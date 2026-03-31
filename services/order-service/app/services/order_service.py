import requests

class OrderService:

    @staticmethod
    def create_order(amount: float):
        response = requests.post(
            "http://payment/payments/",
            json={"amount": amount}
        )

        return {
            "order": "created",
            "payment": response.json()
        }