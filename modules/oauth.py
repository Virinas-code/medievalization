# -*- coding: utf-8 -*-
"""
Medievalization

Google OAuth module
"""
import os.path
from typing import Optional

from google.auth.credentials import Credentials
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as OAuthCredentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES: list[str] = ["https://www.googleapis.com/auth/gmail.send"]
TOKENS_FILE: str = "conf/google/tokens.json"
CREDENTIALS_FILE: str = "conf/google/credentials-web.json"


class GoogleAuth:
    """Main OAuth class."""

    def __init__(self):
        """
        Initialize module.

        Loads tokens.
        """
        self.credentials: Optional[Credentials] = None
        self.flow: InstalledAppFlow = (
            InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        )

    def get_authorization_url(self, redirect_uri: str) -> str:
        """
        Get an URL to redirect user for login.

        :param str redirect_uri: OAuth redirect_uri.
        :return str: Redirect URL.
        """
        if os.path.exists(TOKENS_FILE):
            self.credentials = OAuthCredentials.from_authorized_user_file(
                TOKENS_FILE, SCOPES
            )

        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired:
                self.credentials.refresh(Request())
                return ""

            self.flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES,
                redirect_uri=redirect_uri,
            )
            url, _ = self.flow.authorization_url()
            return url

        return ""

    def get_credentials(self, token: str) -> None:
        """
        Get credentials from token.

        :param str token: Returned token.
        """
        self.flow.fetch_token(code=token)
        self.credentials = self.flow.credentials

        with open(TOKENS_FILE, "w", encoding="utf-8") as file:
            file.write(self.credentials.to_json())
