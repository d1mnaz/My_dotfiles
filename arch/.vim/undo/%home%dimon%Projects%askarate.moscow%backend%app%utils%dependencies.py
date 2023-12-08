Vim�UnDo� ~O�FW�[��F֌n,Ye�iЫ�{b(�����   =       >          
       
   
   
    c���    _�                             ����                                                                                                                                                                                                                                                                                                                                                             c��'     �         7    �         7    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             c��9     �          9    �         9    5�_�                    "   $    ����                                                                                                                                                                                                                                                                                                                            "   $       "   -       v   -    c���     �   !   #   ;      G        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])�   "   #   ;    5�_�                    "   $    ����                                                                                                                                                                                                                                                                                                                            "   $       "   1       v   -    c���     �   !   #   ;      K        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])5�_�                    "   I    ����                                                                                                                                                                                                                                                                                                                            "   $       "   1       v   -    c���     �   !   #   ;      T        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[ALGORITHM])5�_�                    "   Q    ����                                                                                                                                                                                                                                                                                                                            "   $       "   1       v   -    c���    �   >               �       ?       �               ;   	import os   
import sys   2from fastapi import Depends, HTTPException, status   1from fastapi.security import OAuth2PasswordBearer   from jose import JWTError, jwt   (from passlib.context import CryptContext   from sqlmodel import Session       from db.db import get_session   -from db.repositories.users import select_user   3from models.user.user_models import TokenData, User   *from utils.security import verify_password       Lsys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    from core.config import settings   Apwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")       OSECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"   ALGORITHM = "HS256"   ACCESS_TOKEN_EXPIRE_MINUTES = 1       =oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")           async def get_current_user(   K    token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)   ):   *    credentials_exception = HTTPException(   1        status_code=status.HTTP_401_UNAUTHORIZED,   0        detail="Could not validate credentials",   /        headers={"WWW-Authenticate": "Bearer"},       )       try:   ]        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])   *        username: str = payload.get("sub")           if username is None:   '            raise credentials_exception   1        token_data = TokenData(username=username)       except JWTError:   #        raise credentials_exception   ;    user = select_user(username=token_data.username, db=db)       if user is None:   #        raise credentials_exception       return user           Rasync def get_current_active_user(current_user: User = Depends(get_current_user)):       if current_user.disabled:   D        raise HTTPException(status_code=400, detail="Inactive user")       return current_user           Xdef authenticate_user(username: str, password: str, db: Session = Depends(get_session)):   $    user = select_user(username, db)       if not user:           return False   ;    if not verify_password(password, user.hashed_password):           return False       return user5�_�                            ����                                                                                                                                                                                                                                                                                                                               N                 V   Q    c���     �                OSECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"   ALGORITHM = "HS256"5�_�      	                      ����                                                                                                                                                                                                                                                                                                                               N                 V   Q    c���    �                ACCESS_TOKEN_EXPIRE_MINUTES = 15�_�      
           	   1   (    ����                                                                                                                                                                                                                                                                                                                               N                 V   Q    c��z     �   0   2   ;      D        raise HTTPException(status_code=400, detail="Inactive user")5�_�   	               
   ;       ����                                                                                                                                                                                                                                                                                                                               N                 V   Q    c���    �   =               �       >       �               ;   	import os   
import sys   2from fastapi import Depends, HTTPException, status   1from fastapi.security import OAuth2PasswordBearer   from jose import JWTError, jwt   (from passlib.context import CryptContext   from sqlmodel import Session       from db.db import get_session   -from db.repositories.users import select_user   3from models.user.user_models import TokenData, User   *from utils.security import verify_password       Lsys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    from core.config import settings       Apwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")           =oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")           async def get_current_user(   K    token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)   ):   *    credentials_exception = HTTPException(   1        status_code=status.HTTP_401_UNAUTHORIZED,   0        detail="Could not validate credentials",   /        headers={"WWW-Authenticate": "Bearer"},       )       try:           payload = jwt.decode(   K            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]   	        )   *        username: str = payload.get("sub")           if username is None:   '            raise credentials_exception   1        token_data = TokenData(username=username)       except JWTError:   #        raise credentials_exception   ;    user = select_user(username=token_data.username, db=db)       if user is None:   #        raise credentials_exception       return user           Rasync def get_current_active_user(current_user: User = Depends(get_current_user)):       if current_user.disabled:   \        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")       return current_user           Xdef authenticate_user(username: str, password: str, db: Session = Depends(get_session)):   $    user = select_user(username, db)       if not user:           return False   ;    if not verify_password(password, user.hashed_password):           return False       return user5��