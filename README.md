# REEACT FASTAPI based on Python

## User Authentication - SignUp

1. Request Body Fields

    {
        "full_name": "...",
        "email": "...",
        "password": "..."
    }

2. Response

    {
        "user": {
            "full_name": "Ttenochtchi Bush",
            "id": 7,
            "password": "$2b$12$FfQNYj.Hrg3wRX6NI3B4OOQ.4kSo9R8HWGkN1r6qF.zBdGOtzdn0e",
            "updated_at": null,
            "payment_verified": null,
            "subcription_at": null,
            "role": 2,
            "email": "techbush.dev@gmail.com",
            "google_id": null,
            "created_at": "2023-9-13",
            "email_verified": null,
            "subscription_expired": true
        },
        "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ2MTUzMzUuNTg2MDM1N30.LR7FPPqySA0uj9OLOeKoF9fUDQoBui3FPhA-EP1LUY0"
    }

## User Authentication - Login

1. Request Body Fields

    {
        "email": "...",
        "password": "..."
    }

2. Response

    {
        "user": {
            "full_name": "Ttenochtchi Bush",
            "id": 7,
            "password": "$2b$12$FfQNYj.Hrg3wRX6NI3B4OOQ.4kSo9R8HWGkN1r6qF.zBdGOtzdn0e",
            "updated_at": null,
            "payment_verified": null,
            "subcription_at": null,
            "role": 2,
            "email": "techbush.dev@gmail.com",
            "google_id": null,
            "created_at": "2023-9-13",
            "email_verified": null,
            "subscription_expired": true
        },
        "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ2NjExMDcuMDg3NjI4MX0.2X8cb5AYnM7kF9tV_rs0fwi3Hj9HUpTd5k6-rPRccD0"
    }

## Stripe Client Secret

1. Request Body Fields

    {
        "amount": ...
    }

2. Response

    {
        "client_secret": "pi_3Nq4VCHY8rIFJZLc09DIOGUQ_secret_M3ea1x2PCn4HND72OO7wDbdZe"
    }

