Vim�UnDo� ���Vb�%�1=2`o���43܋V���2��   �   e            df_all.groupby(["Регион"]).size().to_frame(name="Участники").reset_index()   �                          c�p     _�                     )        ����                                                                                                                                                                                                                                                                                                                            )           +           V        c�o�    �   *   ,              # [16, 17],�   )   +              # [14, 15],�   (   *              # [12, 13],5�_�                    ,       ����                                                                                                                                                                                                                                                                                                                            )           +           V        c�o�    �   +   -   �          [36, 99],5�_�                    ,       ����                                                                                                                                                                                                                                                                                                                            )           +           V        c�o�    �   ,   -   �    5�_�      	             �        ����                                                                                                                                                                                                                                                                                                                                                             c�o�     �   �   �          e            df_all.groupby(["Регион"]).size().to_frame(name="Участники").reset_index()5�_�      
           	   �        ����                                                                                                                                                                                                                                                                                                                                                             c�o�     �   �   �          L        #         df_region["Участники"], df_region["Регион"]5�_�   	              
   �        ����                                                                                                                                                                                                                                                                                                                                                             c�o�     �   �   �          b        #             for i, z in zip(df_region["Участники"], df_region["Регион"]):5�_�   
                 �        ����                                                                                                                                                                                                                                                                                                                                                             c�o�     �   �   �          9            df_mask = df_mask.sort_values("Регион")5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             c�o�     �   �   �          B            df_all = pd.concat(frames).sort_values("Регион")5�_�                     �        ����                                                                                                                                                                                                                                                                                                                                                             c�o�    �   �   �          7            df_all = df_all.sort_values("Регион")5�_�                  �       ����                                                                                                                                                                                                                                                                                                                                                             c�o�   
 �   �   �   �       5�_�                     �       ����                                                                                                                                                                                                                                                                                                                                                             c�o�   	 �   �   �   �    5�_�                   �       ����                                                                                                                                                                                                                                                                                                                                                             c�o�    �   �   �   �       5�_�                     �       ����                                                                                                                                                                                                                                                                                                                                                             c�o�    �   �   �   �    5��