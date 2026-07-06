from auth.security import (
    create_access_token
)


def authenticate_user(
    username: str,
    password: str
):

    # Demo User

    if (
        username == "admin"
        and password == "admin123"
    ):

        token = create_access_token(
            {
                "sub": username
            }
        )

        return token

    return None