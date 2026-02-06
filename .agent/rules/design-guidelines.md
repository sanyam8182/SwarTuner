---
trigger: always_on
---

# 🤖 System Instructions: "Fluid Minimalism" Design Rules

**Context:** You are an expert React Native developer building a music application.
**Goal:** Implement a UI/UX that is modern, fun, interactive, and clean.
**Tech Stack:** React Native, NativeWind (Tailwind), Reanimated, Expo Blur, Expo Haptics.

Apply the following rules to ALL code generation:

## 1. Visual Geometry & Layout
* **The "No-Divider" Rule:** NEVER use `<View>` borders or divider lines to separate content. Use **Whitespace** (`gap`, `margin`, `padding`) and **Surface Elevation** to define hierarchy.
* **Radius Standardization:**
    * **Containers/Cards:** Always use `rounded-3xl` (approx `24px-32px`).
    * **Buttons:** Always use `rounded-full` (Pill shape).
    * **Small Elements:** Minimum `rounded-2xl` (`16px`).
* **Floating Layouts:** Primary UI elements (Navigation, Players) must **float**. They should never touch the screen edges. Apply `margin-horizontal: 20` and `margin-bottom: 20` (plus Safe Area insets).

## 2. Styling & Colors (NativeWind)
* **Base Palette:**
    * Background: `#080808` (Rich Black) — *Never use pure `#000000`*.
    * Surface: `bg-white/5` (Glass effect).
    * Border: `border-white/10` (Subtle reflection).
* **Glassmorphism:** For overlays, modals, and headers, ALWAYS wrap content in `<BlurView>` (intensity `20-30`, tint `"dark"`).
* **The "Glow" Rule:** Active states (e.g., Playing track, Active Tab) must have a `shadow` that matches the current **Accent Color**.
    * *Example:* `shadow-cyan-500` with `shadow-opacity-50` and `shadow-radius-20`.

## 3. Motion & Physics (Reanimated)
* **Springs Only:** DO NOT use linear `withTiming`. ALL layout transitions and state changes must use `withSpring`.
* **Tactile Buttons:** Wrap all interactive elements in a custom `Pressable` that implements the "Scale Down" effect:
    * `onPressIn`: `scale.value = withSpring(0.96)`
    * `onPressOut`: `scale.value = withSpring(1.0)`
* **Micro-Interactions:** Elements should not just appear; they should `FadeInDown.springify()` or `ZoomIn.springify()`.

## 4. Typography & Readability
* **Font Weights:** Use Extreme Contrast.
    * **Headers:** `font-bold` (700) or `font-black` (900).
    * **Body/Meta:** `font-light` (300) or `font-medium` (500).
* **Metadata Styling:** Secondary text (Artist Name, Time) must be `text-white/60` and have increased tracking (`tracking-widest` for uppercase labels).

## 5. Haptics & Platform specifics
* **Haptic Feedback:** EVERY interactive touch must trigger a haptic response.
    * Import `* as Haptics from 'expo-haptics'`.
    * Use `Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light)` for standard taps.
    * Use `Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium)` for toggles/switches.
* **Safe Areas:** ALWAYS use `useSafeAreaInsets` to determine padding. Never hardcode top/bottom spacing for headers or footers.

---

**Example Component Structure:**
```tsx
<Animated.View className="m-5 rounded-3xl overflow-hidden shadow-lg shadow-purple-500/30">
  <BlurView intensity={30} tint="dark" className="p-6">
    <Text className="text-white font-black text-2xl">Title</Text>
    <Text className="text-white/60 font-light tracking-wide mt-1">Subtitle</Text>
  </BlurView>
</Animated.View>