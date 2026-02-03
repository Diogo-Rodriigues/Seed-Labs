# Return-to-libc Attack Lab

> **IMPORTANT**: The complete resolution, technical details, and step-by-step procedures for this lab are documented in the accompanying **report.pdf**.

## Overview

This lab focuses on bypassing the **Non-executable Stack (NX)** protection, a common security feature that prevents the execution of code injected into the stack. Instead of using shellcode, this attack leverages **Return-to-libc** and **Return-Oriented Programming (ROP)** techniques to redirect program flow to existing legitimate code within the standard C library (`libc`).

---

## 🎯 Objectives

* Understand and bypass **NX/DEP (Data Execution Prevention)** hardware protections.

* Locate and utilize the memory addresses of standard library functions like `system()`, `execv()`, and `exit()`.

* Manipulate the stack to pass specific arguments to `libc` functions.

* Implement a **Return-Oriented Programming (ROP)** chain to execute multiple functions in a specific sequence.

* Defeat shell countermeasures (privilege dropping) in programs like `dash`.

---

## 🧠 Key Concepts & Learnings

### 1. Bypassing NX with Code Reuse

- **The Strategy Shift:** Unlike standard buffer overflows, this attack does not care about the stack address for code execution; it focuses on the **libc text segment addresses**.

- **Function Hijacking:** By overwriting the return address with the address of `system()`, the program can be forced to execute arbitrary commands (e.g., `/bin/sh`) using code already present in memory.

- **Graceful Termination:** Including the `exit()` function address in the payload ensures the program terminates cleanly after the exploit, avoiding suspicious crashes.

### 2. Defeating Shell Countermeasures

- **Privilege Dropping:** Modern shells like `dash` drop root privileges if they detect they are running in a Set-UID process.

- **execv() and the -p Flag:** To preserve privileges, the attack was adapted to use `execv()` to call `/bin/bash` with the `-p` flag.

- **Argument Array Construction:** Learned to manually construct a complex `argv[]` array on the stack, ensuring proper alignment of pointers to strings like `"/bin/bash"` and `"-p"`.

### 3. Return-Oriented Programming (ROP)

- **Function Chaining:** Learned to chain multiple calls by exploiting the `ret` instruction. Each time a function finishes, it pops the next address off the stack and jumps to it.

- **Sequential Execution:** Successfully demonstrated this by invoking an unused `foo()` function 10 times consecutively before launching the root shell.

### 4. Environmental Sensitivity

- **Address Stability:** Discovered that changes in the executable's filename length shift the position of environment variables in memory, which can break exploits relying on hard-coded addresses.

- **Brute-Force Alignment:** Used a brute-force script to account for slight memory offsets between the debugger (`gdb`) and the actual shell environment, ensuring perfect pointer alignment.

---

## 📂 Lab Tasks Summary

| Task | Focus |
| --- | --- |
| **Task 1 & 2** | Identifying `libc` function addresses and placing attack strings in memory (environment variables vs. direct injection).
| **Task 3** | Launching a basic Return-to-libc attack to obtain a root shell by jumping to `system()`.
| **Task 4** | Bypassing `dash` privilege dropping by using `execv()` with the `-p` flag and brute-forcing stack offsets.
| **Task 5** | Building a **ROP chain** to execute `foo()` multiple times before the final exploit.
