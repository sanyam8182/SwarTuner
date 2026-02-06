# Design System: Fluid Minimalism & Artistic Resonance

This document defines the overarching UI/UX principles for the application. The goal is to balance **clean, modern structure** with **expressive, artistic interactions.**

---

## 1. Core Philosophy
* **Depth over Borders:** Use layers, shadows, and blurs to define hierarchy instead of rigid lines or dividers.
* **Physicality:** Elements should react to touch with weight and elasticity (Spring physics).
* **Color as Light:** Treat accent colors as light sources that "glow" onto dark surfaces.

---

## 2. Visual Foundation (The "Look")

### A. Geometry & Radii
To maintain a "fun" yet "clean" aesthetic, avoid sharp corners entirely.
* **Primary Containers:** `32px` corner radius (Squircle/Super-ellipse).
* **Small Components (Buttons/Inputs):** `16px` or fully rounded (Pill-shaped).
* **Media/Images:** Always match the container radius (`16px` to `24px`).

### B. Surface & Color
The app follows a **Dark-First** aesthetic to allow artistic colors to pop.
* **Base Background:** `#080808` (Deep Charcoal).
* **Surface (Cards/Modals):** **Glassmorphism** — `background: rgba(255, 255, 255, 0.05)` with a `20pt-30pt` background blur.
* **Edge Lighting:** Use a `1px` stroke with `10% white` opacity on top edges to simulate light hitting glass.

### C. Typography
* **Primary Typeface:** Geometric Sans-Serif (e.g., *Outfit* or *Lexend*).
* **Contrast:** Use high weight contrast (e.g., `Black 900` for titles vs `Light 300` for subtitles).
* **Editorial Spacing:** Increase letter spacing (`tracking`) for all-caps labels to `10%` to enhance the "modern" feel.

---

## 3. Motion & Interaction (The "Feel")

### A. The "Spring" Standard
All animations must use **Spring Physics** (Damping/Stiffness) rather than linear durations.
* **Tap State:** Scale down to `0.96` on touch-start; pop back to `1.0` on touch-end.
* **Screen Transitions:** Slide-and-Fade with a slight overshoot to create a "bouncy" feel.

### B. Haptic Language
* **Selection:** Single "light" impact feedback.
* **Switch/Toggle:** "Medium" impact.
* **Success/Action:** Double-pulse "soft" haptics.

### C. The Glow Principle
Active elements (icons, sliders, buttons) should emit a **soft outer glow** (Shadow Color = Accent Color, Blur = 15pt) to reinforce the artistic, music-inspired energy.

---

## 4. Platform-Specific Consistency

| Feature | iOS Implementation | Android Implementation |
| :--- | :--- | :--- |
| **Blur** | Native `BlurView` (Vibrant tint) | Skia-based blur or `RenderEffect` |
| **Navigation** | Floating Tab Bar (Safe Area Bottom) | Floating Tab Bar (Elevation + Ripple) |
| **Back Action** | Edge-swipe gesture primary | System back + Edge-swipe |

---

## 5. Artistic Consistency Checklist
- [ ] **No Hard Blacks:** Is the background a deep charcoal rather than `#000`?
- [ ] **No Dividers:** Is content separated by spacing/blur instead of lines?
- [ ] **Soft Shadows:** Are shadows large, diffused, and low-opacity?
- [ ] **Dynamic Accent:** Does the UI pull a single primary color from the active content?
- [ ] **Float Everything:** Do primary UI elements "float" (not touching screen edges)?
