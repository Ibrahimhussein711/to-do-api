# AI vs Me

## How AI Was Used

AI assistance was used during the development of this project for:

- Explaining FastAPI concepts and REST API structure.
- Explaining SQLite and SQL concepts.
- Helping understand CRUD operations.
- Explaining how to connect FastAPI with SQLite.
- Helping troubleshoot errors during development.
- Explaining Git commands and the purpose of commits.
- Helping structure the project documentation.

---

## What I Implemented and Verified

I personally implemented and tested the following parts of the project:

- Created the FastAPI application.
- Created the SQLite database.
- Created the `tasks` table.
- Implemented CRUD endpoints.
- Connected the API to SQLite.
- Tested the endpoints using Swagger UI.
- Tested SQL queries using DB Browser for SQLite.
- Verified that database changes were reflected through the API.
- Tested `404 Not Found` behavior for non-existing tasks.
- Created and tested the project documentation.
- Managed the project using Git and GitHub.

---

## Important Concepts I Learned

During this project, I learned and practiced:

### FastAPI

- Creating a FastAPI application.
- Creating API endpoints using HTTP methods.
- Using path parameters.
- Using Pydantic models for request validation.
- Running an application using Uvicorn.
- Testing APIs through Swagger UI.

### SQLite

- Creating a SQLite database.
- Creating tables.
- Inserting records.
- Selecting records.
- Updating records.
- Deleting records.
- Using primary keys.
- Using SQLite with a Python application.

### SQL

I practiced the following SQL operations:

```sql
SELECT * FROM tasks;
```

```sql
SELECT * FROM tasks
WHERE done = 1;
```

```sql
SELECT COUNT(*) FROM tasks;
```

```sql
UPDATE tasks
SET title = 'Study SQL'
WHERE id = 1;
```

```sql
DELETE FROM tasks
WHERE id = 3;
```

### Git and GitHub

I practiced:

- Creating commits.
- Writing meaningful commit messages.
- Checking Git status.
- Pushing changes to GitHub.
- Maintaining project history.

---

## AI Verification

AI-generated suggestions were reviewed and tested during development.

API behavior was verified using Swagger UI, while database behavior was verified using DB Browser for SQLite and direct SQL queries.

The final implementation was tested locally before being committed and pushed to GitHub.

---

## Conclusion

AI was used as a learning and development assistant, but the project was implemented, tested, and reviewed manually.

The goal was not only to generate code, but also to understand how the API, database, SQL queries, and Git workflow work together.