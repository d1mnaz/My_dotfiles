Vim�UnDo� �wv�I#{����<>}�����d�$�Ч   U       V                           c���    _�                            ����                                                                                                                                                                                                                                                                                                                                         2       v   2    c���     �         Q      4            status_code=status.HTTP_400_BAD_REQUEST,�         Q    5�_�                    .       ����                                                                                                                                                                                                                                                                                                                                         ;       v   2    c���     �   -   .              # return {"user": user}5�_�                    *       ����                                                                                                                                                                                                                                                                                                                                         ;       v   2    c���     �   )   +   P      4            detail="Incorrect username or password",5�_�                    8       ����                                                                                                                                                                                                                                                                                                                                         ;       v   2    c���     �   7   9   P      4            detail="Incorrect username or password",5�_�                     P       ����                                                                                                                                                                                                                                                                                                                                         ;       v   2    c���    �   U               �       V       �               P   =from fastapi import APIRouter, Depends, HTTPException, status   6from fastapi.security import OAuth2PasswordRequestForm   from sqlmodel import Session       from db.db import get_session   :from db.repositories.users import insert_user, select_user   Ifrom models.user.user_models import (Token, TokenRefresh, User, UserBase,   :                                     UserCreate, UserRead)   Ifrom utils.dependencies import authenticate_user, get_current_active_user   Ffrom utils.security import (create_access_token, create_refresh_token,   .                            get_password_hash)       router = APIRouter()           @router.post(       "/",       summary="Create new user",       response_model=UserBase,   (    status_code=status.HTTP_201_CREATED,   )   Lasync def create_user(data: UserCreate, db: Session = Depends(get_session)):   5    user = select_user(username=data.username, db=db)       if user is not None:           raise HTTPException(   =            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,   U            detail="Такой пользователь уже существует",   	        )   4    data.password = get_password_hash(data.password)   (    user = insert_user(user=data, db=db)       return user           /@router.post("/login", response_model=UserRead)   async def login(   X    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)   ):   H    user = authenticate_user(form_data.username, form_data.password, db)       if not user:           raise HTTPException(   5            status_code=status.HTTP_401_UNAUTHORIZED,   M            detail="Неправильный логин или пароль",   3            headers={"WWW-Authenticate": "Bearer"},   	        )       return user           ,@router.post("/token", response_model=Token)   !async def login_for_access_token(   X    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)   ):   H    user = authenticate_user(form_data.username, form_data.password, db)       if not user:           raise HTTPException(   5            status_code=status.HTTP_401_UNAUTHORIZED,   M            detail="Неправильный логин или пароль",   3            headers={"WWW-Authenticate": "Bearer"},   	        )   C    access_token = create_access_token(data={"sub": user.username})   E    refresh_token = create_refresh_token(data={"sub": user.username})       return {   %        "access_token": access_token,   '        "refresh_token": refresh_token,           "token_type": "bearer",       }           +@router.get("/me", response_model=UserRead)   Oasync def read_users_me(current_user: User = Depends(get_current_active_user)):       return current_user           :@router.get("/refresh_token", response_model=TokenRefresh)   Tasync def refresh_user_token(current_user: User = Depends(get_current_active_user)):       if current_user:   O        access_token = create_access_token(data={"sub": current_user.username})           return {   )            "access_token": access_token,   #            "token_type": "bearer",   	        }5��