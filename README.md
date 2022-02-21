# webhook
Pre-Req:
1. Python 3.10 and above
2. Pip

Installation:
1. Clone the repository
2. Install requirements.txt
3. manage.py makemigrations
4. manage.py migrate
5. manage.py createsuperuser
6. manage.py runserver
7. open the url in browser https://<host_server_address>/admin/
8. Login as superuser

Uses:
1. For Authentication: None
   1. use url https://<host_server_address>/webhook_authless/webhook
2. For Authentication: Basic
   1. use url https://<host_server_address>/webhook_auth/webhook
3. For Authentication: API_KEY
   1. use url https://<host_server_address>/webhook_apikey/webhook
