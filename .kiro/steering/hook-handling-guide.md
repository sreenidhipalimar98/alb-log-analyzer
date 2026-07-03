---
inclusion: auto
---

# Hook Handling Guide

## Overview

Hooks in this workspace are configured to provide safety checks before certain operations. They DO NOT block operations — they require acknowledgment before proceeding.

## Critical Rules

1. ALWAYS respond to hook instructions — don't ignore them or ask the user what to do
2. Hooks don't block — they only require acknowledgment before proceeding
3. Be concise — brief acknowledgment is sufficient
4. Then proceed — after acknowledging, immediately execute the original tool call
5. Don't ask permission — the hook just needs your verification, not user approval

## Pattern to follow

Tool call → Hook intercepts (tool NOT executed) → You acknowledge → You call the SAME tool again → Tool executes
