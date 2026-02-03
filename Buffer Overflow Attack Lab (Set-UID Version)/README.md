# Buffer Overflow Set-UID Lab

> **IMPORTANT**: The complete resolution, technical details, and step-by-step procedures for this lab are documented in the accompanying **report.pdf**.


## Overview

This lab explores the fundamental **Buffer Overflow** vulnerability within **Set-UID** privileged programs. The primary goal is to understand how the lack of boundary checking in memory buffers can be exploited to hijack a program's execution flow and gain root access to the system.

---

## 🎯 Objectives

* Understand process memory organization (Stack, Heap, Code).
* Exploit string copying vulnerabilities where length validation is absent (e.g., `strcpy`).
* Develop an **exploit** to inject malicious code (*shellcode*) into the stack.
* Evaluate and bypass system-level protections such as **Non-executable Stack** and **Address Space Layout Randomization (ASLR)**.

---

## 🧠 Key Concepts & Learnings

### 1. Stack Manipulation and the Program Counter

* **Stack Frames:** Deep dive into how function arguments, return addresses, and local variables are stored in memory.
* **Return Address:** Learned how to identify and overwrite the return address to point to the start of the injected *shellcode*.
* **EIP (Instruction Pointer):** Gained understanding of how to take control of the register that determines the CPU's next instruction.

### 2. Exploitation Techniques

* **NOP Sled (NOP Slide):** Used a sequence of `0x90` instructions to increase the exploit's reliability, allowing the jump to the *shellcode* to succeed even without an exact memory address.
* **Shellcode Injection:** The process of writing Assembly code that executes a shell (`/bin/sh`) and embedding it into an attack payload.
* **Offset Calculation:** Calculating the exact distance between the buffer's start and the return address using debugging tools like `gdb`.

### 3. Defenses and Countermeasures

* **Address Space Layout Randomization (ASLR):** Observed how randomizing memory addresses makes predicting the stack's location significantly harder.
* **Stack Guard (Canaries):** Analyzed the compiler’s (`gcc`) role in inserting "sentinel" values to detect stack corruption before a function returns.
* **Non-Executable Stack (NX/DEP):** Studied the protection that prevents code execution in data regions of memory, which necessitates advanced techniques like *Return-to-libc*.

---

## 📂 Lab Tasks Summary

| Task | Focus |
| --- | --- |
| **L1 (Task 3)** | Exploiting the vulnerability with **ASLR disabled**, focusing on the core mechanics of return address hijacking. |
| **L2 (Task 4)** | Attacking the binary when the **buffer size is unknown**, requiring a strategic placement of the return address within the payload. |
| **Task 7** | Bypassing **dash shell protections** by modifying shellcode to call `setuid(0)` before execution. |
| **Task 8** | **Defeating ASLR** on 32-bit systems using a brute-force approach with a shell script. |
| **Task 9** | Evaluating the effectiveness of **StackGuard** and **Non-Executable Stack** in preventing successful exploits. |
