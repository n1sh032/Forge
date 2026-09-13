# FORGE — Project State

## Project
FORGE is a multi-LLM software engineering orchestrator.

The goal is to create a system where multiple LLMs collaborate on software engineering tasks.

Initial model roles:

- GPT = planner / architect / critic
- Claude = implementation / coding agent
- Automated tests = objective verification

---

## Current Goal

Build V1:

User
→ GPT planning
→ Claude implementation
→ GPT critique
→ Claude repair
→ automated verification

The system should eventually iterate until the implementation passes evaluation.

---

## Current Status

Project initialized.

No implementation yet.

---

## Architecture

V1 will initially use plain Python.

Do NOT use LangChain, LangGraph, or another orchestration framework yet.

We want to understand the underlying mechanics ourselves first.

---

## Planned Components

src/
    orchestrator.py

    agents/
        builder.py
        critic.py

    providers/
        claude.py
        openai.py

tests/

---

## Important Rules

1. Never blindly trust an LLM.
2. GPT's criticism must be evaluated rather than automatically accepted.
3. Automated tests should eventually be the objective source of truth.
4. Keep API keys out of source code.
5. Keep the architecture simple until complexity is justified.
6. Every significant implementation should be verified.
7. Do not rewrite unrelated code.

---

## Development History

### Initial setup
- Project created.
- Continuity system established.
- V1 architecture defined.

---

## Current Problem

None.

---

## Next Action

Design the V1 API/provider interfaces and implement the first Claude → GPT pipeline.

---

## Notes for Another AI

If another AI receives this file:

1. Read the entire file.
2. Understand the current architecture.
3. Check the repository before making changes.
4. Continue from "Next Action".
5. Do not restart the project or redesign it without a reason.
6. Update this file when significant decisions, bugs, fixes, or milestones occur.