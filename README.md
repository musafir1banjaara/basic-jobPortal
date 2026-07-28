#Workflow for login

Home Page
    │
    │ GET /
    ▼
index.html
    │
    │ Click Login
    ▼
GET /login/
    │
    ▼
login_user()
    │
    ▼
render(login.html)
    │
    │ User enters credentials
    │
    │ Click Submit
    ▼
POST /login/
    │
    ▼
login_user()
    │
authenticate()
login()
    │
    ▼
redirect("/")
    │
    ▼
GET /
    │
    ▼
home()
    │
    ▼
index.html
(User is now authenticated)