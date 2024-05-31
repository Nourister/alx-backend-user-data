#!/usr/bin/env python3

from typing import List, TypeVar
from flask import Flask, request

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
         """
        Check if authentication is required for the given path.

        Args:
            path (str): The path being accessed.
            excluded_paths (List[str]): List of paths that are excluded from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False


    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header from the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str: The authorization header.
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user based on the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            TypeVar('User'): The current user.
        """
        return None
