# FORGE — Project State

## Purpose

FORGE is a multi-agent AI software engineering system.

The goal is to make multiple AI models collaborate on software development instead of relying on one model.

## Current Goal

Build FORGE V1:

User Task
↓
Planner
↓
Builder
↓
Critic
↓
Repair
↓
Verification

## Current Architecture

For V1, all agents will initially use OpenAI.

The architecture must be designed so other providers such as Claude and Gemini can be added later without rewriting the entire system.

## V1 Agents

### Planner

Converts the user's request into:

* requirements
* implementation plan
* acceptance criteria

### Builder

Takes the plan and implements the requested software changes.

### Critic

Reviews the implementation for:

* correctness
* architecture
* bugs
* security problems
* unnecessary complexity
* missing edge cases
* missing tests

### Repair

Uses the critic's findings to improve the implementation.

## Important Principles

* Do not blindly trust an LLM.
* Automated tests should be treated as stronger evidence than another LLM's opinion.
* Keep V1 simple.
* Use plain Python before adding LangChain, LangGraph, or other orchestration frameworks.
* Keep model providers replaceable.
* Never store API keys in source control.
* Every important change should be verifiable.

## Current Status

Project created.

No implementation has been written yet.

## Next Action

Design the provider interface and basic orchestration flow before implementing the agents.
