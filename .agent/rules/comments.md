---
trigger: always_on
---

# Code Commenting Protocol

## 1. Core Directive
**MANDATORY:** All generated code must include comprehensive inline and block comments. You must prioritize clarity of **intent** over clarity of syntax.

## 2. The "What & Why" Standard
Every comment must answer 4 specific questions:
1.  **WHAT:** What is this specific block of code doing mechanically?
2.  **WHY:** Why does this code exist? (e.g., specific business logic, handling an edge case, performance optimization, or dependency requirement).
3. Any tricky logic
4. TODO items, if there are any.

## 3. Scope of Application
Comments are required for **every instance** of the following:
* **Functions/Methods:** Docstrings or block comments above the definition.
* **Conditionals (`if`/`else`/`switch`):** Explain the criteria and the consequence.
* **Loops (`for`/`while`/`map`):** Explain the iteration goal and exit conditions.
* **Complex Logic:** Any calculation, regex, or non-obvious variable assignment.

## 4. Format Specification
Use the following structure for your comments:

* **For Functions:** Use standard documentation format (e.g., JSDoc, Python Docstrings).
* **For Logic Blocks:** Use the `//` or `#` syntax immediately preceding the line.

### Example Template
```text
// [WHAT]: <Brief description of the action>
// [WHY]: <Reasoning, business context, or specific constraint handling>
```

---

## 5. Examples

### ❌ Incorrect (Too Vague)
```javascript
// Check if user is valid
if (user.status === 'active' && user.role === 'admin') {
    deleteDatabase(); // Delete the DB
}
```

### ✅ Correct (Compliant)
```javascript
/**
 * [WHAT]: Validates user permissions before executing destructive actions.
 * [WHY]: Prevents unauthorized deletion; strict requirement for 'admin' role per Security Protocol 4.2.
 */
function attemptDatabaseDeletion(user) {
    
    // [WHAT]: Check if user is currently active and holds the 'admin' role.
    // [WHY]: Only active admins are authorized to perform hard deletes; prevents accidental deletions by suspended accounts.
    if (user.status === 'active' && user.role === 'admin') {
        
        // [WHAT]: Execute the deletion command on the primary database instance.
        // [WHY]: This is a permanent action required for the 'System Reset' feature requested by the DevOps team.
        deleteDatabase(); 
    }
}
```
## 6. Use JSDoc for functions:
### Example Template
```
/**
 * Calculates user's total points
 * @param userId - The user's ID
 * @returns Total points earned
 */
function func(argOne: string): number {
  // implementation
}
```