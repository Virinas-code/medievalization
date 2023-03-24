# -*- coding: utf-8 -*-
"""
Medievalization

Module to login and send emails.
"""
import base64
import logging
from email.mime.text import MIMEText

from google.auth.credentials import Credentials
from googleapiclient.discovery import Resource, build


def send_mail(
    to_addr: str, subject: str, content: str, *, credentials: Credentials
) -> None:
    """
    Send a mail.

    :param str to_addr: Send to.
    :param str subject: Mail subject.
    :param str content: Mail message.
    :param google.auth.credentials.Credentials credentials:
        OAuth credentials.
    """
    service: Resource = build("gmail", "v1", credentials=credentials)
    message: MIMEText = MIMEText(content)
    message["to"] = to_addr
    message["subject"] = subject
    create_message: dict[str, str] = {
        "raw": base64.urlsafe_b64encode(message.as_bytes()).decode()
    }
    message = (
        service.users()  # type: ignore  # pylint: disable=no-member
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    logging.log(logging.INFO, "Sent message to %s", message)
