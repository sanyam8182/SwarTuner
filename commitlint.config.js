module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'header-max-length': [2, 'always', 50],
    'body-max-line-length': [2, 'always', 72],
    // 'subject-case': [2, 'always', 'sentence-case'], // Optional: Enforce sentence case if desired, but "conventional" usually implies lowercase.
    // Keeping default subject-case from conventional config (lower-case) unless user strictly requested "Imperative" which often implies Sentence case. 
    // The prompt said "Imperative mood" which usually implies "Add feature" (Capitalized). 
    // Let's override to allow sentence-case or header-case to look more "Imperative".
    'subject-case': [0] // Disable case check to allow "Add feature" vs "add feature" flexibility, or enforce specifics if needed.
  },
};
