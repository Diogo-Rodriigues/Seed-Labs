# Environment Variable and Set-UID Program Lab

> **IMPORTANT**: The complete resolution, technical details, and step-by-step procedures for this lab are documented in the accompanying **report.pdf**.

## Overview

This lab explores the impact of **environment variables** on process behavior and the critical security implications they have on **Set-UID programs**. Through a series of tasks, I analyzed how variables are inherited across processes, how dynamic loaders protect privileged binaries, and how improper handling of the environment can lead to privilege escalation.

---

## 🎯 Objectives

* Understand the lifecycle of environment variables: creation, export, and removal.


* Analyze variable inheritance during `fork()`, `execve()`, and `system()` calls.


* Investigate the security measures implemented by the Linux dynamic linker/loader (`ld.so`) for Set-UID binaries.


* Demonstrate and mitigate common vulnerabilities such as **PATH manipulation**, **LD_PRELOAD exploits**, and **Capability Leaking**.



---

## 🧠 Key Concepts & Learnings

### 1. Process Inheritance

- **Forking:** Child processes receive a full copy of the parent's environment variables.

- **Execution (`execve` vs `system`):** * `execve()` does **not** automatically inherit environment variables; they must be explicitly passed via the third argument (`envp`).

- `system()` invokes `/bin/sh`, which automatically inherits the calling process's environment, making it more convenient but significantly less secure.

### 2. Set-UID Security & Sanitization

- **LD_LIBRARY_PATH & LD_PRELOAD:** The dynamic loader automatically ignores these variables when a process's Real UID (RUID) differs from its Effective UID (EUID). This prevents attackers from injecting malicious shared libraries into root-owned programs.

- **Shell Behavior:** Many modern shells (like `dash`) drop privileges (set EUID back to RUID) when they detect they are running in a Set-UID context, providing a defense-in-depth against command injection.

### 3. Vulnerability Patterns

- **PATH Manipulation:** If a Set-UID program uses `system()` to call a command without an absolute path (e.g., `system("ls")`), an attacker can modify the `PATH` variable to point to a malicious binary.

- **Capability Leaking:** This occurs when a privileged program opens a resource (like a file descriptor) and fails to close it before dropping privileges and executing unprivileged code. The open descriptor remains accessible, violating the **Principle of Least Privilege**.

---

## 📂 Lab Tasks Summary

| Task | Focus |
| --- | --- |
| **1-4** | Variable manipulation and inheritance mechanics (`fork`, `execve`, `system`).
| **5-6** | Set-UID behavior and the dangers of `PATH` in privileged contexts.
| **7** | Dynamic loader protections against `LD_PRELOAD`.
| **8** | Comparing `system()` vs `execve()` security.
| **9** | Investigating Capability Leaking via open File Descriptors.

