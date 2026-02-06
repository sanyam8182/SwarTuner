---
trigger: always_on
---

# Rule: Jira & Testing Protocol

* **Context:** Applied when the user asks to work on a specific task or story.
* **Requirement:**
    * Never start coding without an approved **Implementation Plan**.
    * Always check if a Jira ticket exists for the work. If yes, keep its status synced (In Progress -> Done).
    * **Zero-Regression Policy:** No task is "Complete" until Unit Tests AND E2E tests are passing.
    * **Tech Stack Awareness:** When planning, explicitly check for side effects in the specific stack (e.g., "Will this NestJS interceptor change affect other routes?", "Does this Next.js middleware block valid requests?").