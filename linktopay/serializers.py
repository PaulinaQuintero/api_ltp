
from django.contrib.sites import requests
from rest_framework import serializers
from .models import LinkToPayRequest
import logging
import time
import hashlib
from base64 import b64encode
import json

class LinkToPaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkToPayRequest
        fields = '__all__'

    def create(self, data):
        payload = self._prepare_supplier_payload(data)
        server_application_code = 'PAU-MXN-SERVER'
        server_app_key = 'IdHK1C988Hd6iZUtMPEWvqP3C5KuDq'
        unix_timestamp = str(int(time.time()))
        uniq_token_string = server_app_key + unix_timestamp
        uniq_token_hash = hashlib.sha256(uniq_token_string.encode('utf-8')).hexdigest()
        auth_token = (b64encode('%s;%s;%s' % (server_application_code, unix_timestamp, uniq_token_hash))).decode('utf-8')
        headers = {'content-type': 'application/json',
                   'auth-token': 'auth-token {}'.format(auth_token)}


        try:
            response = requests.post("https://noccapi-stg.paymentez.com/linktopay/init_order/", json= payload, headers= headers)

        except requests.exceptions.RequestException:
            logging.error('Error')

        response_json = response.json()
        data["supplier_reference"] = response_json["status"]
        instance = super().create(data)

        return instance

    @staticmethod
    def _prepare_supplier_payload(data):
        partial_payment = bool(1)
        return {
            "user": {
                "id": data["id"],
                "email": "ejemplo@email.com",
                "name": "Señor",
                "last_name": "Prueba"
            },
            "order": {
                "dev_reference": data["dev_reference"],
                "description": "Product description",
                "amount": data["amount"],
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

