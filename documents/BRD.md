# Business Requirements Document (BRD)

**Project Name:** SwarTuner (Indian Classical Vocal Assistant)  
**Date:** February 6, 2026  
**Version:** 1.0  
**Author:** Business Analysis Team  

---

## 1. Executive Summary & Business Need

**Current Market Gap:** Existing vocal learning applications typically fall into one of three categories that fail to meet the specific needs of Indian Classical musicians:
1.  **Western-centric:** Focused on "Equal Temperament" (C, D, E) rather than Indian "Just Intonation" (Swaras/Micro-tones).
2.  **Outdated:** Legacy apps (e.g., *Shruti Carnatic Tuner*) do not function on modern mobile operating systems (Android 14+ / iOS 17+).
3.  **Cost-Prohibitive:** Modern Indian apps (e.g., *Riyaz*) lock essential tuner features behind expensive subscriptions or complex courseware.

**Business Objective:** Develop a standalone, lightweight mobile application that functions as a high-precision "digital ear" for Indian Classical Music students. The app must provide real-time, corrective feedback on pitch using Indian music terminology (Swaras) and harmonic tuning standards.

---

## 2. Target User Personas

* **The Beginner Student:** Unsure of their natural scale (Sa); struggles to differentiate between "Komal" (Flat) and "Shuddh" (Natural) notes; needs visual confirmation that they are hitting the right note.
* **The Practicing Hobbyist:** Knows their scale but needs a reference tool to ensure their practice remains pitch-perfect without an external teacher present.

---

## 3. Functional Requirements (FR)

### Module 1: Scale Configuration (The "Sa" Logic)
**Context:** In Indian music, notes are relative. A "Re" changes frequency based on the chosen "Sa".

* **FR 1.1 - Dynamic Root Note Selection:** The system shall allow users to manually select their Root Note (Sa) from a list of standard keys (e.g., C#, A#, G).
* **FR 1.2 - Automated Scale Detection ("Find My Sa"):** The system shall provide a guided utility to identify the user's natural scale.
    * The user shall be prompted to sing a comfortable sustained note.
    * The system shall analyze the input and recommend the nearest standard scale (e.g., "You are singing at 145Hz, we recommend setting your scale to D").
    * The user must be able to accept or reject this recommendation.

### Module 2: The Core Tuner (Real-Time Feedback)
**Context:** This is the primary screen where the user spends 90% of their time.

* **FR 2.1 - Real-Time Listening:** The application must continuously listen to microphone input when active.
* **FR 2.2 - Note Identification:** As the user sings, the system must identify and display the specific Swara being sung (e.g., Sa, Re, Ga).
    * **Constraint:** The display must use Indian terminology (Swaras), not Western letters.
* **FR 2.3 - Precision Feedback:** The system must indicate *accuracy* relative to the target note.
    * It must clearly communicate three states: **Perfect**, **Sharp** (High), or **Flat** (Low).
    * It must quantify the error (e.g., "High by 10 cents") to help the user adjust.
* **FR 2.4 - Octave Detection:** The system must indicate which octave (Saptak) the user is singing in (Lower/Mandra, Middle/Madhya, or Higher/Taar).

### Module 3: Indian Music Theory Logic
**Context:** The app must distinguish itself from generic tuners by handling the nuances of Indian Ragas.

* **FR 3.1 - Swara Variations:** The system must support and distinguish between the 12 semantic notes of the Indian octave:
    * **Shuddh (Natural):** Re, Ga, Ma, Dha, Ni
    * **Komal (Flat):** Re, Ga, Dha, Ni
    * **Teevra (Sharp):** Ma
* **FR 3.2 - Just Intonation Tuning:** The system shall calculate target frequencies based on harmonic ratios (Just Intonation), not the standard Western "Equal Temperament" formula.
    * *Example:* A "Pa" must be calculated as a perfect 1.5 ratio to "Sa", not the slightly flatter Western "G".

---

## 4. User Interface Requirements (UX Constraints)

* **UX 1 - Visual Simplicity:** The interface must not be cluttered with complex graphs or sheet music. It should focus on a single, clear indicator of pitch accuracy (e.g., a dial, gauge, or traffic light system).
* **UX 2 - Ambiguity Handling:** If a user sings a frequency exactly between two notes (e.g., between Komal Re and Shuddh Re), the visual indicator must reflect this "in-between" state rather than forcing a wrong guess.

---

## 5. Non-Functional Requirements (NFR)

* **NFR 1 - Latency:** The visual feedback must appear with minimal delay (under 50ms) to feel "instant" to the singer.
* **NFR 2 - Compatibility:** The application must function on modern mobile operating systems (Android 14+ and iOS 17+).
* **NFR 3 - Offline Capability:** The core tuner functionality must work without an active internet connection.
* **NFR 4 - Responsiveness:** The UI must adapt to various screen sizes (phones and tablets).

---

## 6. Assumptions & Dependencies

* **Assumption:** The user will practice in a relatively quiet environment (background noise cancellation is a "nice to have," not a core requirement for MVP).
* **Assumption:** The device microphone hardware is sufficient for vocal frequency capture.

---

## 7. Out of Scope (For Phase 1)

* **Gamified Lessons:** No scoring systems, levels, or "Guitar Hero" style gameplay.
* **Raga Guides:** The app will not teach *how* to sing a specific Raga, only *if* the notes are in tune.
* **Recording/Playback:** No feature to record sessions and save them to the cloud.
