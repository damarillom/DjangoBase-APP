import requests

data = {
    "products": [
        {
            "reference": "p1",
            "name": "lslikrsjalbc",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p2",
            "name": "bupceepcikye",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p3",
            "name": "labhgcegthaw",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p4",
            "name": "ghvuqkvylwvp",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p5",
            "name": "qjjjzgodkahg",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p6",
            "name": "fmdvdqrzleky",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p7",
            "name": "qsheccfcrdgxb",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p8",
            "name": "niprfeudenhl",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p9",
            "name": "sojkgrefdfsf",
            "volume": 0.0,
            "created": "2023-01-18"
        },
        {
            "reference": "p10",
            "name": "fsefnrbtuksj",
            "volume": 0.0,
            "created": "2023-01-18"
        }
    ]
}

for p in data['products']: 
    response = requests.post('http://localhost:8000/app/products/', json=p)
    print(response.status_code)