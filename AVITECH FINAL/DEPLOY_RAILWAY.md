# AVITECH deployment (Railway + MySQL)

## 1. Push this project to GitHub
Commit and push the updated files to the `main` branch.

## 2. Create services in Railway
1. Create a Railway project and deploy the `yachivohra/avitech` GitHub repository.
2. Add a MySQL database service.
3. In the Flask service's Variables panel, set:
   - `AVITECH_SECRET_KEY`: a long random secret generated privately
   - `AVITECH_DB_HOST`: reference the MySQL service's `MYSQLHOST`
   - `AVITECH_DB_PORT`: reference `MYSQLPORT`
   - `AVITECH_DB_USER`: reference `MYSQLUSER`
   - `AVITECH_DB_PASSWORD`: reference `MYSQLPASSWORD`
   - `AVITECH_DB_NAME`: reference `MYSQLDATABASE`
   - optionally `AVITECH_ADMIN_EMAIL`: email to designate an administrator
4. The Procfile starts the app with Gunicorn. Generate a public domain in the Flask service's Networking settings.

## 3. Database notes
On first startup, AVITECH creates its application tables in the configured database. It does not create the managed database itself. Existing local data is not automatically uploaded: export the local database from MySQL Workbench and import it into the online database before using the production site if you need to preserve existing records.

## 4. Security
- Do not commit `.env` files or database credentials.
- Do not use GitHub Pages for the Flask backend.
- Verify login, registration, MCQ/theory tests, result saving, and history after deployment.
- This project runs user-submitted coding evaluation logic; use a dedicated isolated sandbox for production-grade execution of untrusted code.
