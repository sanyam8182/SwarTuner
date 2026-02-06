---
description: End-to-end lifecycle management for a user story: from Jira status update to implementation, testing, and final sign-off.
---

## Step 1: Initialization & Jira Sync
* **Input:** Ask the user for the **Jira Issue Key** (e.g., `PROJ-123`) if not provided in the prompt.
* **Action:**
    1.  Fetch the details of the Jira issue.
    2.  Transition the Jira issue status to **"In Progress"**.
    3.  Analyze the requirements against the current project architecture (specifically looking for impacts on NestJS modules, DTOs, or Next.js pages).

## Step 2: Architecture & Planning
* **Action:** Create a Markdown Artifact titled **"Implementation Plan: [Issue Key]"**.
* **Content Requirement:**
    * **Architecture Change:** Detail new modules, schema changes (Postgres/Prisma/TypeORM), or API updates.
    * **Components & State:** Define new Screens, Components, Hooks, or Redux/Context updates.
    * **Navigation:** Detail changes to React Navigation stacks (Deep links? Tab bar visibility?).
    * **Impact Analysis:** List existing features that might be affected.
    * **Native Impact:** Explicitly state if `pod install` or Gradle syncs are needed.
    * **Task Breakdown:** Break the story into granular technical sub-tasks.
* **Gate:** **PAUSE** and ask the user to review and approve the Implementation Plan Artifact. Do not proceed to code until confirmed.

## Step 3: Execution Loop
* **Instruction:** Iterate through the approved tasks one by one.
* **For each task:**
    1.  **Code:** Implement the changes.
    2.  **Unit Test:** Write/Update tests using `Jest` and `Testing Library`.
    3.  **E2E Test:** Update/Run `Detox` or `Appium` tests for critical flows.
    4.  **Verify:** Ensure no layout breakages on different screen sizes.
    5.  **Refine:** If tests fail, debug and retry.

## Step 4: Final Review & Completion
* **Action:**
    1.  Run a final validation of all tests.
    2.  Summarize the changes and test results in the chat.
* **Gate:** **PAUSE** and request final approval from the user to close the ticket.
* **Action (If Approved):**
    1.  Transition the Jira issue status to **"Done"**.
    2.  Output: "Ticket [Issue Key] moved to Done. Implementation complete."