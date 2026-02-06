---
trigger: always_on
---

# Rule: React Native & Jira Protocol

* **Context:** Applied when implementing features or fixing bugs.
* **Requirement:**
    * **Platform Parity:** Always consider "How does this look on Android vs iOS?" during Impact Analysis.
    * **State Management:** When modifying state, check for re-render performance impacts.
    * **Native Code:** If a task requires native module linking (Info.plist, AndroidManifest.xml), explicitly flag this for the user.
    * **Testing:** No task is complete without passing Jest snapshots/unit tests.
    * **Jira Sync:** Maintain strict Jira status discipline (In Progress -> Done).