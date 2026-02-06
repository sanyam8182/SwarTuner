# SwarTuner - Architecture Design Document (ADD)

> **Version:** 1.0  
> **Status:** Draft  
> **Date:** February 6, 2026

---

## 1. Executive Summary

SwarTuner is a high-precision, offline-first mobile application designed for Indian Classical Musicians. Unlike standard Western tuners, it must support **Just Intonation**, **Micro-tonal (Swara) detection**, and significantly lower latency (<50ms) to provide a "Digital Ear" experience.

This architecture prioritizes:
1.  **Low Latency:** Optimized audio buffer processing.
2.  **Modularity:** Separation of DSP (Digital Signal Processing) from UI.
3.  **Fluid UX:** 60fps animations driven by `react-native-reanimated`.
4.  **Cross-Platform Parity:** Singular codebase for Android & iOS using React Native (Expo).

---

## 2. High-Level Design (HLD)

### 2.1 Technology Stack

| Layer | Technology | Choice Rationale |
| :--- | :--- | :--- |
| **Framework** | **React Native (Expo SDK 50+)** | Best-in-class rapid development, OTA updates, and native module support. |
| **Language** | **TypeScript (Strict)** | Type safety is critical for complex music theory logic. |
| **UI System** | **NativeWind (Tailwind CSS)** | Rapid styling, consistent design system tokens. |
| **Animations** | **React Native Reanimated 3** | Main thread animations essential for the "Tuner Gauge". |
| **Audio I/O** | **Expo AV / Audio** | Reliable cross-platform audio stream access. |
| **DSP Engine** | **Pitchy / Custom Wasm** | specialized pitch detection logic (Autocorrelation/YIN). |
| **State Mgmt** | **Zustand** | Minimalist global state (Settings, Theme) without Redux boilerplate. |
| **Persistence** | **MMKV** | Fastest key-value storage for retaining user preferences (Sa, Theme). |

### 2.2 System Architecture Diagram

```mermaid
graph TD
    subgraph "Presentation Layer (UI/UX)"
        UI_Tuner[Tuner Screen]
        UI_Settings[Settings Screen]
        UI_Components[Shared Components]
        
        UI_Tuner --> Anim_Gauge[Reanimated Gauge]
        UI_Tuner --> Anim_Swara[Swara Display]
    end

    subgraph "Application Layer (State & Logic)"
        Store_Settings[Settings Store (Zustand)]
        Store_Session[Tuner Session Store]
        
        Logic_Mapper[Swara Mapper]
        Logic_Theory[Music Theory Engine]
    end

    subgraph "Core Engine (Infrastructure)"
        Audio_IO[Audio Input Manager]
        DSP_Pitch[Pitch Detector (DSP)]
        Storage_MMKV[MMKV Persistence]
    end

    %% Data Flow
    Audio_IO -->|Raw Buffer Float32| DSP_Pitch
    DSP_Pitch -->|Frequency (Hz) + Confidence| Store_Session
    Store_Settings -->|Root Note (Sa)| Logic_Mapper
    Store_Session -->|Current Hz| Logic_Mapper
    Logic_Mapper -->|Swara + Cents| UI_Tuner
    
    %% Persistence
    Store_Settings <--> Storage_MMKV
```

### 2.3 Data Flow Structure

1.  **Input:** Microphone captures audio samples (Chunk size: 2048/4096 frames).
2.  **Processing:**
    *   **DSP:** Algorithm (e.g., McLeod Pitch Method) detects Fundamental Frequency (f0) and Clarity.
    *   **Filtering:** Low-pass filter removes noise; confidence threshold gates weak signals.
3.  **Analysis:**
    *   **Normalization:** $f0$ is compared against the User's Root Note ($Sa$).
    *   **Mapping:** `MusicTheoryEngine` determines the nearest *Just Intonation* interval.
    *   **Quantification:** Deviation (Cents) is calculated: $1200 \times \log_2(f0 / target)$.
4.  **Output:** UI subscribes to the computed state and updates the *Needle* and *Text* via SharedValues (Render Thread).

---

## 3. Low-Level Design (LLD)

### 3.1 Module: Core Audio Engine (`src/engine/audio`)

**Responsibility:** Reliable capture of raw audio data with minimal dropout.

*   **Class: `AudioInputManager`**
    *   `start()`: Requests permissions, configures AudioSession (Measurement Mode).
    *   `subscribe(callback)`: Emits Float32Array buffers.
    *   `stop()`: Cleanly releases hardware resources.
    *   *Constraint:* Must handle "Interruption" events (e.g., incoming call).

*   **Class: `PitchDetector`**
    *   `detect(buffer: Float32Array, sampleRate: number): PitchResult`
    *   **Interface `PitchResult`:** `{ frequency: number, clarity: number }`
    *   *Algorithm:* Use a sliding window average to smooth "jitter" in detection.

### 3.2 Module: Music Theory Engine (`src/engine/theory`)

**Responsibility:** The intelligence/brain of the tuner.

*   **Constants: `JustIntonationRatios`**
    *   Wait-free lookup object mapping Swara Keys to Ratios (e.g., `SA: 1`, `RE_k: 16/15`).

*   **Class: `TuningSystem`**
    *   `concertPitchA4`: Default 440Hz (configurable).
    *   `rootNoteFrequency`: Calculated from User's Key selection.
    *   `getFrequency(ratio)`: Returns target Hz.

*   **Class: `SwaraMapper`**
    *   `getSwara(inputHz)`: Returns `{ swara: string, cents: number, octave: 'Mandra'|'Madhya'|'Taar' }`
    *   *Logic:*
        1.  Determine Octave by doubling/halving Root Frequency.
        2.  Find nearest Ratios in that Octave.
        3.  Interpolate cents deviation.

### 3.3 Module: UI/UX Layer (`src/features/tuner`)

**Responsibility:** 60fps visualization.

*   **Component: `TunerGauge`**
    *   Uses `useSharedValue` for `cents` deviation (-50 to +50).
    *   `useDerivedValue` interpolates Color (Green <-> Red) based on `Math.abs(cents)`.
    *   *Optimization:* No React State updates on the JS thread for needle movement; purely Reanimated.

*   **Component: `SwaraLabel`**
    *   Displays text: "Sa", "Re" (with underline/dots for notation if required).
    *   Reactive to "Lock" state (when user holds a note steady).

### 3.4 Module: Storage & Settings (`src/store`)

*   **Store: `useSettingsStore` (Zustand + MMKV middleware)**
    *   `rootKey`: string (e.g., "C#")
    *   `isExpertMode`: boolean
    *   `theme`: 'dark' | 'light'

---

## 4. Cross-Cutting Concerns

### 4.1 Latency & Performance
*   **Buffer Size:** Target 2048 frames @ 44.1kHz (~46ms latency). Lower buffers risk "crackling" on Android; higher buffers cause visual lag.
*   **Concurrency:** Heavy DSP math should ideally run on a separate Worklet or Thread if JS thread drops frames. (Phase 2 optimization).

### 4.2 Error Handling
*   **No Microphone Access:** Show a strict "Permission Denied" screen with a link to OS settings.
*   **Quiet Input:** If Confidence < 0.8, UI should show a "Listening..." or "Low Signal" state (Ghost Needle).

### 4.3 Offline Support
*   Entire Logic layer is pure TypeScript functions with no API dependencies.
*   Application bundle encompasses all necessary assets (fonts, icons).

## 5. Deployment Strategy
*   **CI/CD:** Github Actions -> Expo EAS Build.
*   **Versioning:** Semantic Versioning (1.0.0).
*   **Environment:** Production builds strip all `console.log` from the DSP loop to prevent bridge congestion.
