# Seed-Labs
---
> **IMPORTANT**: This repository contains my personal solutions and technical reports for the **SEED Labs** (Security Education) project. Each laboratory directory includes a detailed **`report.pdf`** with the complete step-by-step resolution, technical analysis, and screenshots of the successful exploits.

## 📌 Overview

This project was developed as part of the **Computer Systems Security** course at the **University of Minho (2025/2026)**. The goal is to explore fundamental security vulnerabilities, understand how they work at a low level, and implement both exploitation and mitigation strategies in controlled environments.

## 🛠️ Environment & Tools

All labs were performed using the official **SEED Ubuntu pre-built Virtual Machines**.

* **Languages:** C, Python, Shell Script, Assembly.
* **Tools:** `gdb` (with PEDA), `gcc`, `netcat`, `sysctl`.
* **Key Skills:** Memory corruption, privilege escalation, and bypassing OS-level protections.

---

## 📂 Laboratory Collection

### 1. [Environment Variable and Set-UID Program](https://github.com/Diogo-Rodriigues/Seed-Labs/tree/main/Environment%20Variables.%20and%20Set-UID%20Lab)

Exploration of how environment variables affect the behavior of privileged programs.

* **Key Topics:** `fork()` vs `execve()`, `PATH` manipulation, `LD_PRELOAD` exploits, and capability leaking.

### 2. [Buffer Overflow Set-UID Lab](https://www.google.com/search?q=./Buffer_Overflow_Lab)

Deep dive into memory corruption and stack-based overflows to gain root access.

* **Key Topics:** Stack frames, Return Address hijacking, NOP Sleds, and bypassing **ASLR**, **StackGuard**, and **NX**.

### 3. [Return-to-libc Attack Lab](https://www.google.com/search?q=./Return_to_libc_Lab)

Advanced exploitation focusing on bypassing the **Non-executable Stack (NX)** protection.

* **Key Topics:** Code reuse (libc), `system()` vs `execv()`, defeating shell countermeasures (`dash` privilege dropping), and **Return-Oriented Programming (ROP)** chains.

---

## 👥 Authors

* **Diogo Gomes Rodrigues** 

* **José Diogo Azevedo Martins**

* **Tomás Moura Martins dos Santos Ferreira**

## ⚠️ Disclaimer

This repository is for **educational purposes only**. All experiments were conducted in isolated virtual environments. Never use these techniques on systems without explicit authorization.
