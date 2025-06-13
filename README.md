# Assembly Code Interpreter

This project implements a lightweight **assembly language interpreter** written in Python. It reads a text file containing simplified assembly instructions and simulates the execution of each instruction by updating registers and flags accordingly. The results are saved in a separate output file.

### 🧠 Supported Features

* Five core instructions: `ADD`, `SUB`, `MOV`, `AND`, `OR`
* Register support: `EAX`, `EBX`, `ECX`, `EDX` + partial registers (`AX`, `AH`, `AL`, etc.)
* Flags supported:
  * `Carry`
  * `Zero`
  * `Negative`
  * `Overflow`
* Input: free-form, case-insensitive `.txt` file (syntax assumed correct)
* Output: final values of registers and flags saved to output file
* Handles negative numbers and mixed formatting gracefully


