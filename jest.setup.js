/* eslint-env jest */
jest.mock('expo-haptics', () => ({
    NotificationFeedbackType: {
        Success: 'success',
        Warning: 'warning',
        Error: 'error',
    },
    ImpactFeedbackStyle: {
        Light: 'light',
        Medium: 'medium',
        Heavy: 'heavy',
    },
    notificationAsync: jest.fn(),
    impactAsync: jest.fn(),
}));
