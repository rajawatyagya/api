import os
from templated_mail.mail import BaseEmailMessage

from django.contrib.auth.tokens import default_token_generator
from djoser import utils, conf

from iboxz.settings import BASE_DIR


class CustomActivationEmail(BaseEmailMessage):
    template_name = os.path.join(BASE_DIR, 'templates', 'email', 'activation.html')

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super(CustomActivationEmail, self).get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = conf.settings.ACTIVATION_URL.format(**context)
        return context
