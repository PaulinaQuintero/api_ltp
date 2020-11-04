import requests
from rest_framework import serializers
from .models import LinkToPayRequest
import logging
import time
import hashlib
from base64 import b64encode


class LinkToPaySerializer(serializers.ModelSerializer):
    id=serializers.CharField(max_length=100)
    dev_reference=serializers.CharField(max_length=100)
    amount=serializers.FloatField()
    class Meta:
        model = LinkToPayRequest
        fields = ('id', 'dev_reference', 'amount')

    def create(self, validated_data):
        print(validated_data)
        payload = self._prepare_supplier_payload(validated_data)
        server_application_code = 'PAU-MXN-SERVER'
        server_app_key = 'IdHK1C988Hd6iZUtMPEWvqP3C5KuDq'

        unix_timestamp = str(int(time.time()))
        uniq_token_string = server_app_key + unix_timestamp
        uniq_token_hash = hashlib.sha256(uniq_token_string.encode()).hexdigest()
        msg = '%s;%s;%s' % (server_application_code, unix_timestamp, uniq_token_hash)
        auth_token = b64encode(msg.encode())
        headers = {'content-type': 'application/json',
                   'auth-token': 'auth-token {}'.format(auth_token)}


        try:
            response = requests.post("https://noccapi-stg.paymentez.com/linktopay/init_order/", json= payload, headers= headers)
            logging.info(response)
            response_json = response.json()
            logging.info(response_json)
            print(response_json["payment_url"])


        except Exception as e:
            logging.error(e)

        instance = super().create(validated_data)
        return instance



    @staticmethod
    def _prepare_supplier_payload(validated_data):
        partial_payment = bool(1)
        print(partial_payment)
        return {
            "user": {
                "id": validated_data["id"],
                "email": "ejemplo@email.com",
                "name": "Señor",
                "last_name": "Prueba"
            },
            "order": {
                "dev_reference": validated_data["dev_reference"],
                "description": "Product description",
                "amount": validated_data["amount"],
                "installments_type": 0,
                "currency": "MXN"
            },
            "configuration": {
                "partial_payment": partial_payment,
                "expiration_days": 1,
                "allowed_payment_methods": ["All", "Cash", "BankTransfer", "Card"],
                "success_url": "https://url-to-success.com",
                "failure_url": "https://url-to-failure.com",
                "pending_url": "https://url-to-pending.com",
                "review_url": "https://url-to-review.com"
            }
        }

