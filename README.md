# PROG8850 Assignment 4: Database Automation

This project demonstrates database automation using **Ansible**, **Flyway**, and **GitHub Actions** for schema migrations and validation, as required for PROG8850 Assignment 4.

## Project Structure

- `up.yaml` — Ansible playbook to start MySQL (in Docker) and run Flyway migrations.
- `down.yaml` — Ansible playbook to dump the database and stop MySQL.
- `sql/` — Flyway migration scripts (`V1__init_schema.sql`, `V2__add_subscription_date.sql`, etc.).
- `dbtests.py` — Python script to validate the database schema.
- `requirements.txt` — Python dependencies.
- `backup.sql` — (Generated) Database dump after running `down.yaml`.

---

## Prerequisites

- **Docker** (pre-installed in GitHub Codespaces)
- **Python 3** (pre-installed in Codespaces)
- **Ansible** (pre-installed in Codespaces)
- **Flyway** (used via Docker)
- **MySQL Connector for Python** (installed via `requirements.txt`)

---

## Setup & Usage

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start MySQL and Apply Migrations

```bash
ansible-playbook up.yaml
```

- This will start a MySQL Docker container and apply all Flyway migrations in the `sql/` directory.

### 3. Validate the Database Schema

```bash
python dbtests.py
```

- This script checks that the `subscriber` table exists and includes the `email` and `subscription_date` columns.

### 4. (Optional) Manually Test Data Insertion

To verify that `subscription_date` is auto-populated:

```bash
docker exec -it mysql-db mysql -uflyway -pflywaypass subscribers
```
Then in the MySQL prompt:
```sql
INSERT INTO subscriber (email) VALUES ('test@example.com');
SELECT * FROM subscriber;
```

### 5. Dump Data and Stop MySQL

```bash
ansible-playbook down.yaml
```

- Dumps the database to `backup.sql` and stops the MySQL container.

---

## Troubleshooting

- If you encounter connection issues with Flyway, ensure the MySQL container is running and the user is set to use `mysql_native_password`.
- If you see YAML errors, ensure your `.yaml` files are properly formatted (no extra `---` except at the top, correct indentation).
