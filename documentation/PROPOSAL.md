# Project Proposal: {PROGRAM_NAME}

## 1. Project Overview
**{PROGRAM_NAME}** is an automated security utility designed to identify and mask **Personally Identifiable Information (PII)** within unstructured text files. In modern data environments, sharing logs or databases for testing often leads to unintended data leaks. This system serves as a "Privacy Shield," ensuring that sensitive data is redacted locally before any document is shared or analyzed.

## 2. Core Aim
The primary objective of {PROGRAM_NAME} is to protect **Data Privacy** and ensure **Security Compliance**. By converting "sensitive" files into "safe" documents, the system prevents unauthorized access to private information while maintaining the original file's structural integrity.

## 3. Key Features
* **Automated Pattern Detection:** Uses logic to identify data like emails, phone numbers, and credit card patterns without manual intervention.
* **Secure Data Obfuscation:** Replaces sensitive strings with descriptive placeholders (e.g., `[REDACTED_EMAIL]`).
* **Non-Destructive Processing:** Implements a safety protocol that generates a new sanitized file, leaving the original source code or data untouched.
* **Data Integrity:** Maintains the context of the file while removing the risk, allowing the document to be used for debugging or analysis safely.

## 4. Technical Implementation
The system is built as a **Logic Engine** focusing on three core pillars of Computer Programming 2:

### A. Pattern Recognition (Regex)
The engine utilizes **Regular Expressions (Regex)** to define complex search patterns. This allows the program to recognize any email or ID format regardless of the specific text content.

### B. File Stream Processing (File I/O)
The implementation follows a strict **Input/Output Stream** protocol:
1.  **Read:** Opens a `FileReader` or `StreamReader` to parse the source file line-by-line.
2.  **Transform:** Each line is processed through the Redaction Engine.
3.  **Write:** The sanitized lines are written to a new file using a `FileWriter`.

### C. Object-Oriented Design (OOP)
The project follows a modular architecture. A base `Redactor` class can be inherited to create specialized modules (e.g., `FinancialRedactor`, `IdentityRedactor`), ensuring the code is organized, reusable, and easy to maintain.

## 5. Team Division & Roles
Our team follows a **Lead-and-Support** structure to maximize productivity across different skill levels:

| Role                                | Responsibility                | Key Tasks                                                                        |
|:------------------------------------|:------------------------------|:---------------------------------------------------------------------------------|
| **Project Architect (Experienced)** | **Core Engine & Logic**       | Development of Regex patterns and the primary Redaction Algorithm.               |
| **I/O Lead (Semi-Experienced)**     | **System Integration**        | Handling File Streams, managing memory efficiency, and coordinating code merges. |
| **UI Designer (Beginner)**          | **User Interface**            | Designing the GUI (buttons, file choosers, and status labels).                   |
| **Validation Lead (Beginner)**      | **Error Handling**            | Writing guard clauses to prevent crashes and ensuring valid user inputs.         |
| **Data & QA Manager (Beginner)**    | **Testing & Documentation**   | Creating mock "dirty" files for testing and documenting the system's usage.      |

## 6. Practical Real-World Application
{PROGRAM_NAME} is a functional tool modeled after professional cybersecurity software. It is applicable in:
* **Healthcare/Finance:** Sanitizing client records before auditing.
* **Software Development:** Redacting server logs before sending them to external support teams.
* **Legal:** Preparing documents for public release while protecting witness or client privacy.