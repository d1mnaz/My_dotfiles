Vim�UnDo� a`�ji���ؚ`'�����>�1K:hc)�[�8Y�                     ;       ;   ;   ;    e�   5 _�                             ����                                                                                                                                                                                                                                                                                                                                                             e�E    �                   5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             e�E     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�T    �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e�^    �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�h    �               Dapp = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�i    �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�j    �             5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             e�k    �             5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             e�m   	 �             5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             e�m   
 �             5�_�   
                    '    ����                                                                                                                                                                                                                                                                                                                                                             e�o    �             5�_�                       8    ����                                                                                                                                                                                                                                                                                                                                                             e�q    �             5�_�                       >    ����                                                                                                                                                                                                                                                                                                                                                             e�q    �             5�_�                       @    ����                                                                                                                                                                                                                                                                                                                                                             e�r    �             5�_�                       B    ����                                                                                                                                                                                                                                                                                                                                                             e�s     �             5�_�                       C    ����                                                                                                                                                                                                                                                                                                                                                             e�v    �               yapp = FastAPI(title="Проведение соревнований"docs_url="/api/docs", openapi_url="/api/openapi.json")5�_�                       F    ����                                                                                                                                                                                                                                                                                                                                                             e�w    �             5�_�                       C    ����                                                                                                                                                                                                                                                                                                                                                             e�x    �             5�_�                       D    ����                                                                                                                                                                                                                                                                                                                                                             e�y    �             5�_�                       E    ����                                                                                                                                                                                                                                                                                                                                                             e�z     �             5�_�                    	        ����                                                                                                                                                                                                                                                                                                                            	                     V   .    e�~    �      	          app = FastAPI(   8    title="Упрощенный аналог Jira/Asana"   )    5�_�                    	        ����                                                                                                                                                                                                                                                                                                                            	          	           V   .    e��    �                  �              �                  import uvicorn   from fastapi import FastAPI   2from fastapi.middleware.cors import CORSMiddleware       #from api.routers import all_routers       {app = FastAPI(title="Проведение соревнований", docs_url="/api/docs", openapi_url="/api/openapi.json")           for router in all_routers:       app.include_router(router)           if __name__ == "__main__":   ,    uvicorn.run(app="main:app", reload=True)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V   .    e��    �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e@e    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e@e     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e@g    �                5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e@g     �         #    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e@j     �                    "http://127.0.0.1:5000",5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e@k    �                    "https://askarate.moscow",5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e@m    �                    "http://localhost",5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e@n    �                    "http://127.0.0.1",5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             e@o    �                    "http://localhost:5000",5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                                                             e@�    �             5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                             e@�    �                   �             5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                             e@�     �             5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             e@�    �                    allow_origins=["*"],5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                             e@�     �             �             5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             e@�   ! �                   "http://localhost:3000",5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                             eA"   " �                   "http://localhost:8000",5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                             eA$   # �             5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                                                             eA$   $ �             5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                             eA%   % �             5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                             eA&   & �             5�_�   +   -           ,          ����                                                                                                                                                                                                                                                                                                                                                             eA'   ' �             5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                                                             eA(   ( �             5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                                                             eA(   ) �             5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                             eA)   * �             5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                                                             eA*     �             5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                             eA.   + �             �             5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                                                             eA1   , �                    "http://127.0.0.1:8000",5�_�   2   4           3   
       ����                                                                                                                                                                                                                                                                                                                                                             e��   - �   
           5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                                                             e��   . �   
      !          �         !    5�_�   4   6           5          ����                                                                                                                                                                                                                                                                                                                                                             e��   / �         !    5�_�   5   7           6          ����                                                                                                                                                                                                                                                                                                                                                             e��   0 �         !    5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                                                             e��   1 �         !    5�_�   7   9           8      	    ����                                                                                                                                                                                                                                                                                                                                                             e��   2 �         !    5�_�   8   :           9          ����                                                                                                                                                                                                                                                                                                                                                             e��   3 �         !    5�_�   9   ;           :          ����                                                                                                                                                                                                                                                                                                                                                             e��     �         !    5�_�   :               ;          ����                                                                                                                                                                                                                                                                                                                                                             e�   5 �   
                 echo=True5��