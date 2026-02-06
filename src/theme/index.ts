import * as Haptics from 'expo-haptics';

export const COLORS = {
    background: '#080808',
    surface: 'rgba(255, 255, 255, 0.05)',
    white: '#FFFFFF',
    white10: 'rgba(255, 255, 255, 0.1)',
    white60: 'rgba(255, 255, 255, 0.6)',
    // Helper for glassmorphism
    glass: 'rgba(255, 255, 255, 0.05)',
};

export const SPRING_CONFIG = {
    damping: 10,
    stiffness: 100,
    mass: 1,
    overshootClamping: false,
    restDisplacementThreshold: 0.01,
    restSpeedThreshold: 2,
};

export const HAPTICS = {
    selection: () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light),
    switch: () => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium),
    success: () => Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success),
    impact: (style: Haptics.ImpactFeedbackStyle) => Haptics.impactAsync(style),
};
