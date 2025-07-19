# 🎲 Random Fake Data Generator API

A FastAPI-powered service that generates realistic random data for testing, automation, and development. Perfect for frontend/backend testing, seeding databases, UI mockups, and more.

---

## 🚀 Features

- 📧 Random Email Addresses  
- 🆔 UUIDs  
- 👤 Full Names  
- 📝 Sentences  
- 📅 Dates (custom formats supported)  
- 🔢 Numbers (integer or float)  
- 🌐 IPv4 Addresses  

You can generate **up to 100 items per request** for any supported type.

---

## 📦 Tech Stack

- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Faker](https://faker.readthedocs.io/)
- Uvicorn (ASGI Server)

---

## 🔧 Installation

```bash
git clone https://github.com/Shabari-K-S/Random-Data-Generator-API.git
cd Random-Data-Generator-API
pip install -r requirements.txt
````

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

Open your browser at:
`http://localhost:8000/docs` – to explore the Swagger UI.

---

## 📌 API Endpoint: `/generate`

Generate fake data dynamically by specifying the type and optional parameters.

### Supported Query Parameters

| Name     | Type   | Required | Description                                                                    |
| -------- | ------ | -------- | ------------------------------------------------------------------------------ |
| `type`   | string | ✅ Yes    | Data type: `email`, `uuid`, `name`, `sentence`, `date`, `number`, `ip_address` |
| `count`  | int    | ❌ No     | Number of items to generate (default: `1`, max: `100`)                         |
| `format` | string | ❌ No     | Custom format for `date` (e.g. `%d/%m/%Y`) or `number` (`integer` or `float`)  |

---

### 📥 Example Request

```
GET /generate?type=name&count=3
```

### 📤 Sample Response

```json
{
  "data_type": "name",
  "generated_items": [
    "Liam Robinson",
    "Olivia Scott",
    "Ethan Turner"
  ]
}
```

---

## 💡 Author

Built by [Shabari-K-S](https://github.com/Shabari-K-S)
Contributions welcome! 🙌

---

Empower your development with dynamic fake data — fast, reliable, and fully customizable.


