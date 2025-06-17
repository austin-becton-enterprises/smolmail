# Becton Enterprises Naming Convention Guide

## Python Naming Guidelines

### General Python Naming Guidelines
- Be consistent across the project or codebase.
- Use descriptive, readable names over short or cryptic ones.
- Use English words unless localization is required.
- Prefer lowercase, underscores, or CamelCase as per context.

### Project & Package Structure
- **Project Name**: lowercase-hyphenated (e.g., `inventory-tracker`)
- **Package Name**: lowercase (e.g., `bectonutils`)
- **Module Name**: lowercase_with_underscores (e.g., `file_reader.py`)

### Naming Elements
- **Variables**: `lower_case_with_underscores` (e.g., `employee_id`)
- **Constants**: `ALL_CAPS_WITH_UNDERSCORES` (e.g., `MAX_RETRIES`)
- **Functions**: `lower_case_with_underscores` (e.g., `send_email_report`)
- **Classes**: `CamelCase` (e.g., `InventoryManager`)
- **Methods**: `lower_case_with_underscores` (e.g., `update_stock_level`)
- **Class/Instance Vars**: `lower_case_with_underscores` (e.g., `self.client_name`)
- **Private/Internal**: `_prefix` (e.g., `_validate_email`)

### Testing
- Test files match module names prefixed with `test_` (e.g., `test_inventory.py`)
- Use descriptive test function names (e.g., `test_total_price_calculation`)

### Becton-Specific Prefixes/Tags
- **Internal APIs**: `becton_api_*`
- **Utility Modules**: `becton_utils_*`
- **Common Models**: `BectonBaseModel`

### Do Not Use
- One-letter variable names like `x`, `y` (except for loops)
- Ambiguous names like `data`, `info`, `stuff`
- Hungarian notation or type prefixing (e.g., `str_name`, `int_count`)

### Optional Tools
- **Linters**: `flake8`, `pylint`
- **Formatters**: `black`, `isort`
- **Pre-commit Hooks**: Enforce rules on commit

---

## 🔧 Git Naming Guidelines

### Branch Naming
- <type>/<short-description>

- Use lowercase and hyphens.
- Keep names short but meaningful.

**Types:**
- `feature/` – New features (`feature/user-authentication`)
- `bugfix/` – Bug fixes (`bugfix/cart-total-error`)
- `hotfix/` – Urgent production fixes (`hotfix/payment-failure`)
- `release/` – Release versions (`release/v1.2.0`)
- `test/` – Experimental code (`test/load-balancer-poc`)
- `docs/` – Documentation (`docs/update-readme`)
- `refactor/` – Refactors (`refactor/cleanup-models`)

### Commit Messages
- <type>: <short summary>

**Examples:**
- `feat: add user login functionality`
- `fix: resolve checkout crash when cart is empty`
- `docs: update API usage instructions in README`

**Commit Types:**
- `feat` – A new feature
- `fix` – A bug fix
- `docs` – Documentation changes
- `style` – Code style fixes
- `refactor` – Code improvements without behavioral changes
- `test` – Adding or updating tests
- `chore` – Minor updates like dependencies or tooling

### Tags & Releases
Follow Semantic Versioning:
- v<MAJOR>.<MINOR>.<PATCH>


Examples:
- `v1.0.0` – First release
- `v1.1.0` – Feature updates
- `v1.1.1` – Bug fixes

### Pull Request Titles
- Clear and concise:
  - `Add search filter to product page`
  - `Fix payment form validation`
  - `Refactor order controller for clarity`
- Reference issues:
  - `Closes #42`

