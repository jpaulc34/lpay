from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordHandler:

    def hash(self, password: str):
        return pwd_context.hash(password)
    
    def verify(password: str, hashed_password: str):
        return pwd_context.verify(password, hashed_password)
    
    def token_data(user):
        return {
            "sub": user.username,
            "hsh": PasswordHandler.hash(user.username),
            "secret": user.password
        }