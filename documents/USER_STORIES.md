# SwarTuner - User Stories

> **Source:** [BRD.md](file:///f:/Development/SwarTuner/SwarTuner/documents/BRD.md)  
> **Date:** February 6, 2026

---

## Epic 1: Scale Configuration (The "Sa" Logic)

### US-1.1: Manual Root Note Selection
**As a** practicing musician,  
**I want to** manually select my Root Note (Sa) from a list of standard Western keys,  
**So that** all subsequent Swaras are calculated relative to my chosen scale.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | A dropdown/picker displays all 12 standard keys: C, C#, D, D#, E, F, F#, G, G#, A, A#, B |
| 2 | The selected key is persisted across app sessions |
| 3 | Selecting a new key immediately recalculates all Swara target frequencies |
| 4 | Default selection is C (261.63 Hz) on first launch |

---

### US-1.2: Automated Scale Detection ("Find My Sa")
**As a** beginner student,  
**I want to** use a guided utility that detects my natural comfortable singing pitch,  
**So that** I can set my Sa without needing to know Western music theory.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | A dedicated "Find My Sa" button/flow is accessible from settings or onboarding |
| 2 | The app displays clear instructions: "Sing a comfortable, sustained note" |
| 3 | The app listens for at least 2 seconds of stable pitch input before analysis |
| 4 | The app calculates the average frequency of the sustained note |
| 5 | The app recommends the nearest standard scale (e.g., "You sang ~147Hz. We recommend D") |
| 6 | The recommendation shows both the detected Hz and the suggested key |
| 7 | User can **Accept** (sets Sa to recommended key) or **Reject** (returns to manual selection) |
| 8 | If audio is too unstable/quiet, display: "We couldn't detect a clear note. Please try again in a quieter environment." |

---

## Epic 2: Core Tuner (Real-Time Feedback)

### US-2.1: Real-Time Microphone Listening
**As a** user,  
**I want** the app to continuously listen to microphone input when the tuner screen is active,  
**So that** I receive immediate feedback as I sing.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | Microphone permission is requested on first access with clear rationale |
| 2 | Audio capture begins automatically when the tuner screen is displayed |
| 3 | Audio capture pauses when the app goes to background or screen is navigated away |
| 4 | A visual indicator (e.g., pulsing mic icon) shows the app is actively listening |
| 5 | If permission is denied, display: "Microphone access is required for the tuner to work" with a button to open settings |

---

### US-2.2: Swara Identification Display
**As a** user,  
**I want** the app to identify and display the specific Swara I am singing using Indian terminology,  
**So that** I can learn and practice in the context of Indian Classical Music.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | The detected Swara is displayed prominently in the center of the tuner screen |
| 2 | Display uses **Indian Swara names only**: Sa, Re (Komal/Shuddh), Ga (Komal/Shuddh), Ma (Shuddh/Teevra), Pa, Dha (Komal/Shuddh), Ni (Komal/Shuddh) |
| 3 | Western note equivalents (C, D, E...) are **not** shown |
| 4 | When no audio is detected, display a neutral state (e.g., "--" or a dimmed indicator) |
| 5 | Swara updates in real-time with latency under 50ms (see NFR-1) |

---

### US-2.3: Pitch Accuracy Feedback (Perfect/Sharp/Flat)
**As a** user,  
**I want** the tuner to show whether I am singing the note perfectly, too high (sharp), or too low (flat),  
**So that** I can correct my pitch in real-time.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | A visual indicator (dial, gauge, needle, or LED-style bar) shows pitch deviation |
| 2 | Three distinct states are visually clear: **Perfect** (center/green), **Sharp** (right/high indicator), **Flat** (left/low indicator) |
| 3 | The deviation is quantified in **cents** (e.g., "+12 cents", "-8 cents") |
| 4 | "Perfect" is defined as within ±5 cents of the target frequency |
| 5 | Colors: Green for Perfect, Orange/Yellow for slight deviation, Red for significant deviation (>25 cents) |

---

### US-2.4: Octave (Saptak) Detection
**As a** user,  
**I want** the tuner to indicate which octave I am singing in,  
**So that** I can practice transitioning between Mandra, Madhya, and Taar Saptaks.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | The current Saptak is displayed alongside the Swara name |
| 2 | Three Saptaks are supported: **Mandra** (Lower), **Madhya** (Middle), **Taar** (Higher) |
| 3 | Display uses Indian terminology: "Mandra", "Madhya", "Taar" (optionally with English labels for beginners) |
| 4 | Saptak changes are reflected immediately as the user transitions octaves |

---

## Epic 3: Indian Music Theory Logic

### US-3.1: Support for All 12 Swara Variations
**As a** user,  
**I want** the app to correctly identify and distinguish all 12 notes of the Indian octave,  
**So that** I can practice Komal, Shuddh, and Teevra variations accurately.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | The system recognizes and maps all 12 semantic notes: |
|   | - Sa (fixed) |
|   | - Komal Re, Shuddh Re |
|   | - Komal Ga, Shuddh Ga |
|   | - Shuddh Ma, Teevra Ma |
|   | - Pa (fixed) |
|   | - Komal Dha, Shuddh Dha |
|   | - Komal Ni, Shuddh Ni |
| 2 | Each Swara variation is displayed with its qualifier (e.g., "Komal Re", not just "Re") |
| 3 | The frequency boundaries between adjacent Swaras are correctly calculated |

---

### US-3.2: Just Intonation Tuning (Harmonic Ratios)
**As a** user,  
**I want** the app to use Just Intonation (harmonic ratios) instead of Equal Temperament,  
**So that** my practice aligns with the tonal purity of Indian Classical Music.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | All Swara frequencies are calculated using Just Intonation ratios relative to Sa |
| 2 | The following ratios are used (relative to Sa = 1): |
|   | - Sa: 1 |
|   | - Komal Re: 16/15 |
|   | - Shuddh Re: 9/8 |
|   | - Komal Ga: 6/5 |
|   | - Shuddh Ga: 5/4 |
|   | - Shuddh Ma: 4/3 |
|   | - Teevra Ma: 45/32 |
|   | - Pa: 3/2 |
|   | - Komal Dha: 8/5 |
|   | - Shuddh Dha: 5/3 |
|   | - Komal Ni: 9/5 |
|   | - Shuddh Ni: 15/8 |
| 3 | Equal Temperament is **not** used |
| 4 | Calculated frequencies are verified against known Just Intonation tables |

---

## Epic 4: User Interface & Experience

### US-4.1: Visual Simplicity (Tuner Interface)
**As a** user,  
**I want** the tuner interface to be clean and focused,  
**So that** I am not distracted by complex graphs or sheet music during practice.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | The tuner screen contains only: Swara display, accuracy indicator (dial/gauge), Saptak indicator |
| 2 | No sheet music, complex waveforms, or multi-layered graphs are shown |
| 3 | The design uses a single, clear focal point for pitch accuracy (e.g., a centered dial or gauge) |
| 4 | Font sizes are large and readable from arm's length (for hands-free practice) |

---

### US-4.2: Ambiguity Handling (In-Between Notes)
**As a** user,  
**I want** the app to visually indicate when I am singing between two notes,  
**So that** the display doesn't force an incorrect guess and confuse me.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | When the sung frequency is within the "boundary zone" between two adjacent Swaras (e.g., between Komal Re and Shuddh Re), the UI reflects this ambiguity |
| 2 | The indicator may show both candidate notes (e.g., "Re? / Re") or a "between" visual state |
| 3 | The accuracy indicator (dial/gauge) shows the position relative to both notes |
| 4 | No single Swara is "snapped to" when the input is genuinely ambiguous |

---

## Epic 5: Non-Functional Requirements

### US-5.1: Low-Latency Feedback (<50ms)
**As a** user,  
**I want** the visual feedback to appear instantly (under 50ms),  
**So that** I can make real-time corrections to my pitch.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | Time from audio input to UI update is measured and verified to be <50ms |
| 2 | Pitch detection algorithm is optimized for speed (e.g., using FFT with small window) |
| 3 | UI updates are scheduled at 60fps to prevent visual lag |

---

### US-5.2: Offline Capability
**As a** user,  
**I want** the core tuner to work without an internet connection,  
**So that** I can practice anywhere, anytime.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | All pitch detection and Swara calculation happens on-device |
| 2 | No network requests are made for core tuner functionality |
| 3 | The app launches and functions fully in Airplane Mode |

---

### US-5.3: Responsive UI (Phones & Tablets)
**As a** user,  
**I want** the app to adapt to my device's screen size,  
**So that** I can use it on my phone or tablet comfortably.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | Layout adapts to portrait and landscape orientations |
| 2 | UI elements scale appropriately for screens from 5" to 12" |
| 3 | Touch targets are at least 44x44 points for accessibility |
| 4 | Tested on at least 3 device sizes: small phone, large phone, tablet |

---

### US-5.4: Platform Compatibility
**As a** user,  
**I want** the app to work on my modern Android or iOS device,  
**So that** I am not excluded due to my choice of platform.

#### Acceptance Criteria
| # | Criterion |
|---|-----------|
| 1 | App runs on Android 14+ |
| 2 | App runs on iOS 17+ |
| 3 | Core functionality is consistent across both platforms |

---

## Out of Scope (Phase 1)

> [!NOTE]
> The following are explicitly **not** included in Phase 1 user stories:
> - Gamified Lessons (scoring, levels, "Guitar Hero" gameplay)
> - Raga Guides (teaching *how* to sing a Raga)
> - Recording/Playback (saving sessions to cloud)
