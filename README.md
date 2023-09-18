# REEACT FASTAPI based on Python

## User Authentication - SignUp(POST)

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

## User Authentication - Login(POST)

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

## Update User with ID(PUT)

1. Request Header

    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ3MDI5OTguMzQyODc2N30.4X4VNd90iAIdQegoiGqv0EtChDB9HtFHU0BfW5TSjKg

2. Request URL with param for user id - user/update/{user_id}

3. Response

    {
        "updated_user": {
            "password": "$2b$12$6oWtWs6Onf2s/DsLKkR3Wed9WUIflpm1TncaUxNwYKLxzBqa9yvUW",
            "id": 2,
            "full_name": "Ttenochtchi Bush",
            "updated_at": "2023-9-14",
            "payment_verified": null,
            "subcription_at": null,
            "role": 2,
            "google_id": null,
            "email": "tenochbush@gmail.com",
            "created_at": "2023-9-14",
            "email_verified": null,
            "subscription_expired": 2
        }
    }

## Stripe Client Secret(POST)

1. Request Header
    
    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ3MDI5OTguMzQyODc2N30.4X4VNd90iAIdQegoiGqv0EtChDB9HtFHU0BfW5TSjKg

2. Request Body Fields

    {
        "amount": ...
    }

3. Response

    {
        "client_secret": "pi_3Nq4VCHY8rIFJZLc09DIOGUQ_secret_M3ea1x2PCn4HND72OO7wDbdZe"
    }

## Payment Log Save(POST)

1. Request Header

    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ3MDI5OTguMzQyODc2N30.4X4VNd90iAIdQegoiGqv0EtChDB9HtFHU0BfW5TSjKg

2. Request Body Fields

    {
        "user_id": 6,
        "amount": 29,
        "currency_type": "usd",
        "payment_type": "paypal",
        "status": "pending"
    }

3. Response

    {
        "payment_log": {
            "user_id": 6,
            "currency_type": "usd",
            "status": "pending",
            "created_at": "2023-9-14",
            "payment_type": "paypal",
            "id": 3,
            "amount": 29
        }
    }

## Google Search with keyword(GET) - /googleSearch/{key_word}?start={start_num}&num={limit}

1. Request Header

    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ3MDI5OTguMzQyODc2N30.4X4VNd90iAIdQegoiGqv0EtChDB9HtFHU0BfW5TSjKg

2. Request Parameters

    keyword, start_num, limit

3. Response

    {
        "search_id": "6507a408f8f5f7a298f4d6c3",
        "status": "Search successfully!!!"
    }

4. In this request, sentiment is handled with the result of Google Search API with snippet.

    Google Search Result has the below fields

        - search_id
        - title
        - link
        - snippet
    
    Sentiment Result has the below fiels

        - keyword
        - label
        - score

    Keyword = Snippet

## Get Sentiment Analaysis Reslts(GET)

1. Request Header

    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ3MDI5OTguMzQyODc2N30.4X4VNd90iAIdQegoiGqv0EtChDB9HtFHU0BfW5TSjKg

2. Request parameters

    page=1&limit=10

3. Response

    [
        {
            "label": "neutral",
            "title": "Fun Facts About Lions • African Lion Information For Kids",
            "link": "https://www.folly-farm.co.uk/zoo/meet-the-zoo-animals/african-lion/",
            "snippet": "Find out more about African lions, including where do they live? What do they eat? How long do they sleep for? Lots of fun facts for kids!",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Lion Movie",
            "link": "https://www.facebook.com/LionMovie/",
            "snippet": "Lion Movie. 236783 likes · 14 talking about this. Adapted from the non-fiction book A Long Way Home by Saroo Brierley, LION is about a five-year-old...",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Lion - definition of lion by The Free Dictionary",
            "link": "https://www.thefreedictionary.com/lion",
            "snippet": "Define lion. lion synonyms, lion pronunciation, lion translation, English dictionary definition of lion. n. 1. A large carnivorous feline mammal of Africa ...",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Lion - Wiki - Golden",
            "link": "https://golden.com/wiki/Lion-XK5XX",
            "snippet": "Final Fight of the Lion King in Epic Battle Full Movie | Wildest Africa - Epic Wildlife Videos. https://www.youtube.com/watch?v=6WvJoSbtnN4.",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Lion Brand Yarn: Yarn and Free Knitting and Crochet Patterns",
            "link": "https://www.lionbrand.com/",
            "snippet": "Lion Brand Yarn is America's oldest craft yarn company with 80+ active yarn families. Find your next project by searching over 8000 free knitting and ...",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Where do lions live? Facts about lions' habitats and other ...",
            "link": "https://www.usatoday.com/story/news/2023/01/08/where-do-lions-live-habitat/10927",
            "snippet": "The Asiatic lion lives in the Gir Forest of western India. And while you might assume that the African lions from west and central Africa are ...",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Disney THE LION KING | On Broadway Since 1997",
            "link": "https://lionking.com/",
            "snippet": "Disney's official site for tickets to the landmark Broadway musical THE LION KING in New York City and on tour across North America.",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Asiatic lions",
            "link": "https://www.londonzoo.org/whats-here/animals/asiatic-lion",
            "snippet": "Asiatic lion facts. There are only several hundred Asiatic lions in the wild, and they only live in the Gir Forest, India, in an area that is smaller than ...",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Detroit Lions Football - Lions News, Scores, Stats, Rumors ...",
            "link": "https://www.espn.com/nfl/team/_/name/det/detroit-lions",
            "snippet": "Visit ESPN to view the latest Detroit Lions news, scores, stats, standings, rumors, and more.",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        },
        {
            "label": "neutral",
            "title": "Lion - LDOCE",
            "link": "https://www.ldoceonline.com/dictionary/lion",
            "snippet": "lion meaning, definition, what is lion: a large animal of the cat family that li...: Learn more.",
            "created_at": "2023-9-17",
            "updated_at": "2023-9-17"
        }
    ]

## Handle Intervention Request(POST)

1. Request Header

    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ3MDI5OTguMzQyODc2N30.4X4VNd90iAIdQegoiGqv0EtChDB9HtFHU0BfW5TSjKg

2. Request Body

    {
        "information": "This is for the test of intervention request"
    }

3. Response

    true

## Handle Messaging Request(POST)

1. Request Header

    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ3MDI5OTguMzQyODc2N30.4X4VNd90iAIdQegoiGqv0EtChDB9HtFHU0BfW5TSjKg

2. Request Body

    {
        "messaging": "This is for the test of messaging"
    }

3. Response

    true

## Get Payment Logs(GET) - /get_paymentLog?start=1&limit=10

1. Request Header

    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidGVjaGJ1c2guZGV2QGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTQ3MDI5OTguMzQyODc2N30.4X4VNd90iAIdQegoiGqv0EtChDB9HtFHU0BfW5TSjKg

2. Request parameters

    start, limit

3. Response

    [
        {
            "user_id": 6,
            "description": "This is for the test of payment Log Save",
            "payment_type": "paypal",
            "created_at": "2023-9-14",
            "currency_type": "usd",
            "id": 1,
            "amount": 29,
            "status": "pending"
        },
        {
            "user_id": 6,
            "description": "This is for the test of Payment Log Save",
            "payment_type": "paypal",
            "created_at": "2023-9-14",
            "currency_type": "usd",
            "id": 2,
            "amount": 29,
            "status": "pending"
        },
        {
            "user_id": 6,
            "description": "fsdf fdsfdsa fdsfsda",
            "payment_type": "paypal",
            "created_at": "2023-9-14",
            "currency_type": "usd",
            "id": 3,
            "amount": 29,
            "status": "pending"
        },
        {
            "user_id": 6,
            "description": "This is for the test of payment Log Save",
            "payment_type": "paypal",
            "created_at": "2023-9-18",
            "currency_type": "usd",
            "id": 4,
            "amount": 29,
            "status": "pending"
        },
        {
            "user_id": 6,
            "description": "This is for the test of payment Log Save",
            "payment_type": "paypal",
            "created_at": "2023-9-18",
            "currency_type": "cads",
            "id": 5,
            "amount": 29,
            "status": "pending"
        },
        {
            "user_id": 6,
            "description": "Hello, World!",
            "payment_type": "paypal",
            "created_at": "2023-9-18",
            "currency_type": "cads",
            "id": 6,
            "amount": 29,
            "status": "pending"
        }
    ]




