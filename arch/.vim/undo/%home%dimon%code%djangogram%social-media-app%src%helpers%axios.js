Vim�UnDo� ���u�KJV�t����Y*뙺':����u�   =                  .       .   .   .    d�@�   # _�                             ����                                                                                                                                                                                                                                                                                                                                                             d�'
    �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d�'
     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d�'    �             �               !baseURL: "http://localhost:8000",   
headers: {   #"Content-Type": "application/json",   },5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d�'    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d�'    �         	    5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             d�'�    �   	               �   	            5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d�'�    �               5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             d�'�     �               5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             d�'�    �             �               /**   3* Retrieving the access token from the localStorage   +and adding it to the headers of the request   */   const { access } =   )JSON.parse(localStorage.getItem("auth"));   2config.headers.Authorization = `Bearer ${access}`;   return config;5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             d�'�     �               -    JSON.parse(localStorage.getItem("auth"));5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             d�'�    �               ,   JSON.parse(localStorage.getItem("auth"));5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d�'�   	 �             �                 /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */     const { access } =   +  JSON.parse(localStorage.getItem("auth"));5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d�(1   
 �                  �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d�(2    �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d�(3     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d�(5    �             �                 /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */     const { access } =   -    JSON.parse(localStorage.getItem("auth"));   4  config.headers.Authorization = `Bearer ${access}`;     return config;   });       'axiosService.interceptors.response.use(   (res) => Promise.resolve(res),   (err) => Promise.reject(err),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d�(s    �                  �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d�(s    �               5�_�                    3       ����                                                                                                                                                                                                                                                                                                                                                             d�(t     �   3            5�_�                    3       ����                                                                                                                                                                                                                                                                                                                                                             d�(u    �         /    �         3        /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */5�_�                    3       ����                                                                                                                                                                                                                                                                                                                                                             d�(�    �   3               �   3            5�_�                    5        ����                                                                                                                                                                                                                                                                                                                                                             d�(�    �   5            5�_�                    :       ����                                                                                                                                                                                                                                                                                                                                                             d�(�     �   :            5�_�                    :       ����                                                                                                                                                                                                                                                                                                                                                             d�(�    �      9       �         :   -     /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */     const { access } =   -    JSON.parse(localStorage.getItem("auth"));   4  config.headers.Authorization = `Bearer ${access}`;     return config;   });       'axiosService.interceptors.response.use(      (res) => Promise.resolve(res),     (err) => Promise.reject(err),   );           3const refreshAuthLogic = async (failedRequest) => {     return axios   
    .post(         "/auth/refresh/",         {   #        refresh: getRefreshToken(),         },         {   -        baseURL: "http://localhost:8000/api",         }       )       .then((resp) => {   #      const { access } = resp.data;   >      failedRequest.response.config.headers["Authorization"] =           "Bearer " + access;         localStorage.setItem(           "auth",   O        JSON.stringify({ access, refresh: getRefreshToken(), user: getUser() })         );       })       .catch(() => {   &      localStorage.removeItem("auth");       });   };       *createAuthRefreshInterceptor(axiosService,   refreshAuthLogic);   export function fetcher(url) {   5return axiosService.get(url).then((res) => res.data);5�_�                    6       ����                                                                                                                                                                                                                                                                                                                                                             d�(�    �   4   6   :      *createAuthRefreshInterceptor(axiosService,   refreshAuthLogic);�   5   7   :        refreshAuthLogic);5�_�                    5   *    ����                                                                                                                                                                                                                                                                                                                                                             d�(�    �   5   6   9    5�_�                    5   +    ����                                                                                                                                                                                                                                                                                                                                                             d�(�     �   5   6   9    5�_�                    5   *    ����                                                                                                                                                                                                                                                                                                                                                             d�(�    �         5    �         9        /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */5�_�                    5   *    ����                                                                                                                                                                                                                                                                                                                                                             d�(�    �   5   7   9    5�_�                    6        ����                                                                                                                                                                                                                                                                                                                                                             d�(�     �   6   7   :    5�_�                     6        ����                                                                                                                                                                                                                                                                                                                                                             d�(�    �         6    �         :        /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */5�_�      !               7       ����                                                                                                                                                                                                                                                                                                                                                             d�)    �   6   8   :      export function fetcher(url) {5�_�       "           !   7   
    ����                                                                                                                                                                                                                                                                                                                                                             d�)    �   7   8   :    5�_�   !   #           "   7   	    ����                                                                                                                                                                                                                                                                                                                                                             d�)    �   7   8   :    5�_�   "   $           #   7       ����                                                                                                                                                                                                                                                                                                                                                             d�)	     �   7   8   :    5�_�   #   %           $   7       ����                                                                                                                                                                                                                                                                                                                                                             d�)    �         6    �         :        /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */5�_�   $   &           %   9        ����                                                                                                                                                                                                                                                                                                                                                             d�)    �   9   ;   :    5�_�   %   '           &   :        ����                                                                                                                                                                                                                                                                                                                                                             d�)     �   :   ;   ;    5�_�   &   (           '   :        ����                                                                                                                                                                                                                                                                                                                                                             d�)    �         7    �         ;        /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */5�_�   '   )           (   -   #    ����                                                                                                                                                                                                                                                                                                                                                             d�)}    �         7    �         ;        /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */5�_�   (   *           )   6        ����                                                                                                                                                                                                                                                                                                                                                             d�<�    �         7    �         ;        /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */5�_�   )   +           *           ����                                                                                                                                                                                                                                                                                                                                       ;           V        d�?�     �                  import axios from "axios";�             :   >import createAuthRefreshInterceptor from "axios-auth-refresh";       #const axiosService = axios.create({   #  baseURL: "http://localhost:8000",     headers: {   '    "Content-Type": "application/json",     },   });       9axiosService.interceptors.request.use(async (config) => {     /**   5  * Retrieving the access token from the localStorage   -  and adding it to the headers of the request     */     const { access } =   -    JSON.parse(localStorage.getItem("auth"));   4  config.headers.Authorization = `Bearer ${access}`;     return config;   });       'axiosService.interceptors.response.use(      (res) => Promise.resolve(res),     (err) => Promise.reject(err),   );           3const refreshAuthLogic = async (failedRequest) => {     return axios   
    .post(         "/auth/refresh/",         {   #        refresh: getRefreshToken(),         },         {   -        baseURL: "http://localhost:8000/api",         }       )       .then((resp) => {   #      const { access } = resp.data;   >      failedRequest.response.config.headers["Authorization"] =           "Bearer " + access;         localStorage.setItem(           "auth",   O        JSON.stringify({ access, refresh: getRefreshToken(), user: getUser() })         );       })       .catch(() => {   &      localStorage.removeItem("auth");       });   };       =createAuthRefreshInterceptor(axiosService, refreshAuthLogic);       $export async function fetcher(url) {   7  return axiosService.get(url).then((res) => res.data);   }       export default axiosService;5�_�   *   ,           +           ����                                                                                                                                                                                                                                                                                                                                                  V        d�?�   ! �                   �               5�_�   +   -           ,   =        ����                                                                                                                                                                                                                                                                                                                                       >           V        d�?�     �   =            5�_�   ,   .           -   =        ����                                                                                                                                                                                                                                                                                                                                       >           V        d�@    " �         :    �         =        /**   D   * Retrieving the access and refresh tokens from the local storage      */5�_�   -               .   =        ����                                                                                                                                                                                                                                                                                                                                       >           V        d�@�   # �         :    �         =        /**   D   * Retrieving the access and refresh tokens from the local storage      */5��