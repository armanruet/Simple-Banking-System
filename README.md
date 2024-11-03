# 🏦 Advanced Banking System

A robust Python-based banking system simulation that implements real-world banking operations with secure card management and transaction handling. This project showcases modern software development practices, including SQL database integration, secure payment card validation (Luhn algorithm), and object-oriented programming principles.

## 🌟 Features

- 🔐 Secure account creation with PIN protection
- 💳 Credit card number generation with Luhn algorithm validation
- 💰 Balance management and transactions
- 🔄 Money transfers between accounts
- 📊 SQLite database integration for persistent storage
- 🛡️ Account closure functionality
- 💵 Income addition capability

## 🏗️ System Architecture

### Component Diagram
```mermaid
graph TB
    UI[User Interface Layer]
    BL[Business Logic Layer]
    DL[Data Layer]
    
    UI --> |User Input/Output| BL
    BL --> |Account Operations| DL
    BL --> |Card Validation| DL
    BL --> |Transaction Management| DL
    DL --> |SQLite Storage| DB[(Database)]
    
    subgraph "Business Logic Components"
        BL --> CardGen[Card Generator]
        BL --> Auth[Authentication]
        BL --> Trans[Transaction Handler]
        BL --> Valid[Validator]
    end
    
    style UI fill:#f9f,stroke:#333,stroke-width:2px
    style BL fill:#bbf,stroke:#333,stroke-width:2px
    style DL fill:#bfb,stroke:#333,stroke-width:2px
    style DB fill:#fbb,stroke:#333,stroke-width:2px
```

### Database Schema
```mermaid
erDiagram
    CARD {
        int id PK
        string number
        string pin
        int balance
    }
```

## 🔄 User Flow

```mermaid
stateDiagram-v2
    [*] --> MainMenu
    MainMenu --> CreateAccount: Select 1
    MainMenu --> Login: Select 2
    MainMenu --> Exit: Select 0
    
    CreateAccount --> GenerateCard
    GenerateCard --> GeneratePIN
    GeneratePIN --> SaveAccount
    SaveAccount --> MainMenu
    
    Login --> AccountMenu: Valid Credentials
    Login --> MainMenu: Invalid Credentials
    
    AccountMenu --> CheckBalance: Select 1
    AccountMenu --> AddIncome: Select 2
    AccountMenu --> Transfer: Select 3
    AccountMenu --> CloseAccount: Select 4
    AccountMenu --> Logout: Select 5
    AccountMenu --> Exit: Select 0
    
    CheckBalance --> AccountMenu
    AddIncome --> AccountMenu
    Transfer --> AccountMenu
    CloseAccount --> MainMenu
    Logout --> MainMenu
    Exit --> [*]
```

## 🛠️ Technical Implementation

### Card Number Generation Process
```mermaid
graph LR
    A[Start] --> B[Generate IIN]
    B --> C[Generate Account Identifier]
    C --> D[Calculate Checksum]
    D --> E[Combine Components]
    E --> F[Validate with Luhn]
    F --> G[Store in Database]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#bfb,stroke:#333,stroke-width:2px
```

### Luhn Algorithm Implementation
The system implements the Luhn algorithm (also known as the "modulus 10" or "mod 10" algorithm) for credit card number validation:

1. Double every second digit from right to left
2. If doubling results in a two-digit number, add those digits together
3. Add all single-digit numbers together
4. If the total modulo 10 is equal to 0, the number is valid

## 🔐 Security Features

- PIN encryption
- Luhn algorithm validation
- Session management
- SQL injection prevention
- Balance protection mechanisms

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/armanruet/Simple-Banking-System.git
```

2. Install dependencies:
```bash
cd Simple-Banking-System
pip install sqlite3
```

3. Run the application:
```bash
python adv_banking.py
```

## 💡 Usage Examples

### Creating a New Account
```python
1. Create an account
2. Log into account
0. Exit
> 1

Your card has been created
Your card number:
4000009455217826
Your card PIN:
6948
```

### Making a Transfer
```python
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
> 3

Enter receiver's card number:
> 4000003305160034
Enter how much money you want to transfer:
> 500
Success! Money has been transferred.
```

## 🔍 Code Structure

```mermaid
graph TD
    Main[Main Application] --> BS[BankingSystem Class]
    BS --> ACC[Account Management]
    BS --> VAL[Validation Logic]
    BS --> DB[Database Operations]
    
    ACC --> Create[Create Account]
    ACC --> Login[Login Handler]
    ACC --> Trans[Transaction Handler]
    
    VAL --> Luhn[Luhn Algorithm]
    VAL --> Pin[PIN Validator]
    
    DB --> SQLite[SQLite Operations]
    DB --> CRUD[CRUD Functions]
    
    style Main fill:#f96,stroke:#333,stroke-width:2px
    style BS fill:#96f,stroke:#333,stroke-width:2px
    style DB fill:#6f9,stroke:#333,stroke-width:2px
```

## 🛣️ Future Roadmap

- [ ] Multi-currency support
- [ ] Transaction history
- [ ] Account statements
- [ ] Interest calculation
- [ ] Joint accounts
- [ ] Mobile number linking
- [ ] Email notifications
- [ ] Two-factor authentication

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- SQLite for providing a robust embedded database
- The Python community for excellent documentation
- Contributors who helped improve the codebase

## 📞 Contact

For any queries or suggestions, please reach out to:
- Email: armanruet@gmail.com
- LinkedIn: [armanruet](https://www.linkedin.com/in/armanruet/)

---
Made with ❤️ by [Arman](https://armanruet.github.io/)