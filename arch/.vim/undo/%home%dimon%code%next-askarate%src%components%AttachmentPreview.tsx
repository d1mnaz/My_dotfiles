Vim�UnDo� a���QK�䵔�O������~|�T	�b{   9   Ximport { FastApiDeleteAttachment } from "@/app/(site)/(blog)/posts/_components/service";      -      M       M   M   M    d��x   H _�                             ����                                                                                                                                                                                                                                                                                                                               	       &   	       V   	    d�u�    �      '   9    �         9    5�_�                       $    ����                                                                                                                                                                                                                                                                                                                            '   	       8   	       V   	    d�u�    �         K      .            {attachments instanceof Array && (5�_�                       $    ����                                                                                                                                                                                                                                                                                                                            '   	       8   	       V   	    d�u�    �         K      )            {attachments instanceof  && (�         K    5�_�                       %    ����                                                                                                                                                                                                                                                                                                                            '   	       8   	       V   	    d�u�    �         K    5�_�                       )    ����                                                                                                                                                                                                                                                                                                                            '   	       8   	       V   	    d�u�    �         K    5�_�                       *    ����                                                                                                                                                                                                                                                                                                                            '   	       8   	       V   	    d�u�     �         K    5�_�                            ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    d�u�    �                6                        attachments.map((file, i) => (   9                            <li key={i} className="my-2">5�_�      	              "       ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    d�u�    �   !   #   I                              ))}5�_�      
           	   !       ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    d�u�     �       !          !                            </li>5�_�   	              
   "       ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    d�u�    �   !   "                          </ul>5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                 V       d�u�   	 �                '                                </Link>   *                                <XMarkIcon   4                                    onClick={() => {   ?                                        deleteAttachment(file);   &                                    }}   �                                    className="mb-1 inline-block h-8 w-8 cursor-pointer justify-end p-1 text-black text-red-600 transition duration-200 hover:scale-125 hover:text-red-800"   "                                />5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�u�   
 �      A       �         A   )   6                                <Link href={file.url}>   k                                    {decodeURIComponent(file.url).substring(file.url.lastIndexOf("/") + 1)}   '                                </Link>                           )}               )}   .            {attachments instanceof Array && (   &                <ul className="mb-10">   #                    {attachments &&   6                        attachments.map((file, i) => (   9                            <li key={i} className="my-2">   6                                <Link href={file.url}>   k                                    {decodeURIComponent(file.url).substring(file.url.lastIndexOf("/") + 1)}   '                                </Link>   *                                <XMarkIcon   4                                    onClick={() => {   ?                                        deleteAttachment(file);   &                                    }}   �                                    className="mb-1 inline-block h-8 w-8 cursor-pointer justify-end p-1 text-black text-red-600 transition duration-200 hover:scale-125 hover:text-red-800"   "                                />   !                            </li>                           ))}                   </ul>               )}   !            {attachmentsPrev && (   &                <ul className="mb-10">   '                    {attachmentsPrev &&   :                        attachmentsPrev.map((file, i) => (   5                            <li key={i} className="">   +                                {file.name}   *                                <XMarkIcon   4                                    onClick={() => {   6                                        onClick(file);   &                                    }}   �                                    className="mb-1 inline-block h-8 w-8 cursor-pointer justify-end p-1 text-black text-red-600 transition duration-200 hover:scale-125 hover:text-red-800"   "                                />   !                            </li>                           ))}                   </ul>               )}           </div>       );5�_�                           ����                                                                                                                                                                                                                                                                                                                            A          A          V       d�u�    �                &                <ul className="mb-10">5�_�                           ����                                                                                                                                                                                                                                                                                                                            @          @          V       d�v	    �         @                              )}5�_�                       #    ����                                                                                                                                                                                                                                                                                                                            @          @          V       d�v    �         @      #                    {attachments &&5�_�                       $    ����                                                                                                                                                                                                                                                                                                                            @          @          V       d�v    �         @    5�_�                       %    ����                                                                                                                                                                                                                                                                                                                            @          @          V       d�v    �         @    5�_�                           ����                                                                                                                                                                                                                                                                                                                            A          A          V       d�v    �         A    5�_�                           ����                                                                                                                                                                                                                                                                                                                            B          B          V       d�v     �         B    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       d�v    �                .                        <Link href={file.url}>   c                            {decodeURIComponent(file.url).substring(file.url.lastIndexOf("/") + 1)}                           </Link>5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�v    �         ?    �         ?    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�v    �      B       �         B   ,   %                    {attachments && (   .                        <Link href={file.url}>   c                            {decodeURIComponent(file.url).substring(file.url.lastIndexOf("/") + 1)}                           </Link>                           )                           }               )}   6                    {attachments instanceof Array && (   .                        <ul className="mb-10">   +                            {attachments &&   >                                attachments.map((file, i) => (   A                                    <li key={i} className="my-2">   >                                        <Link href={file.url}>   s                                            {decodeURIComponent(file.url).substring(file.url.lastIndexOf("/") + 1)}   /                                        </Link>   2                                        <XMarkIcon   <                                            onClick={() => {   G                                                deleteAttachment(file);   .                                            }}   �                                            className="mb-1 inline-block h-8 w-8 cursor-pointer justify-end p-1 text-black text-red-600 transition duration-200 hover:scale-125 hover:text-red-800"   *                                        />   )                                    </li>   #                                ))}                           </ul>                       )}   )                    {attachmentsPrev && (   .                        <ul className="mb-10">   /                            {attachmentsPrev &&   B                                attachmentsPrev.map((file, i) => (   =                                    <li key={i} className="">   3                                        {file.name}   2                                        <XMarkIcon   <                                            onClick={() => {   >                                                onClick(file);   .                                            }}   �                                            className="mb-1 inline-block h-8 w-8 cursor-pointer justify-end p-1 text-black text-red-600 transition duration-200 hover:scale-125 hover:text-red-800"   *                                        />   )                                    </li>   #                                ))}                           </ul>                       )}                   </div>               );5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       d�vV    �                "                { attachments && (   *                    <Link href={file.url}>   _                        {decodeURIComponent(file.url).substring(file.url.lastIndexOf("/") + 1)}                       </Link>                       )                           }5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�vZ    �         ;    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�v[    �         <                      �         <    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�v\    �         <    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�v]    �         <                      <span>�         <    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�v^     �         <    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�v`    �         <                      <span></span>5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       d�v`    �         <    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       d�vb    �         <    5�_�      !                  "    ����                                                                                                                                                                                                                                                                                                                                                V       d�vd    �         <    5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�    �         <    5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�    �         =          �         =    5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�    �         =    5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�     �         =    5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   ! �         =    5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   " �         =    5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   # �         =    5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   $ �         =    5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   % �         =    5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   & �         =    5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�     �         =    5�_�   +   -           ,          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   ' �         =    5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   ( �         >                      �         >    5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   ) �         >    5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   * �         >    5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   + �         >    5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   , �         >    5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   - �         >    5�_�   2   4           3          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   . �         >    5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   / �         >    5�_�   4   6           5           ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   0 �         >    5�_�   5   7           6      !    ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   1 �         >    5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   2 �         ?    5�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�     �         @    5�_�   8   :           9          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   3 �                *                <span>{attachments}</span>5�_�   9   ;           :           ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   4 �         ?    �         ?    5�_�   :   <           ;           ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   5 �                 5�_�   ;   =           <          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   6 �         ?                      )}5�_�   <   >           =           ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   7 �         ?      !                {attachments && (5�_�   =   ?           >          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   8 �         >    �         ?                       {attachments && 5�_�   >   @           ?          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   9 �                                 { attachments &&5�_�   ?   A           @          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   : �                                }5�_�   @   B           A          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   ; �         =      /            {attachments instanceof String && (5�_�   A   C           B          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   < �         =    5�_�   B   D           C          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   = �         =    5�_�   C   E           D          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   > �         =    5�_�   D   F           E          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   ? �         =    5�_�   E   G           F          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   @ �         =    5�_�   F   H           G          ����                                                                                                                                                                                                                                                                                                                                                V       d�v�     �         =    5�_�   G   I           H      #    ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   A �         =      :            {new String(attachments instanceof String && (5�_�   H   J           I      $    ����                                                                                                                                                                                                                                                                                                                                                V       d�v�   B �         =    5�_�   I   K           J           ����                                                                                                                                                                                                                                                                                                                               !                 V   !    d�w   C �                ;            {new String(attachments) instanceof String && (   *                <span>{attachments}</span>               )}5�_�   J   L           K          ����                                                                                                                                                                                                                                                                                                                               !                 V   !    d�we   E �                    console.log(attachments)5�_�   K   M           L      -    ����                                                                                                                                                                                                                                                                                                                                                             d��s   F �         9      Ximport { FastApiDeleteAttachment } from "@/app/(site)/(blog)/posts/_components/service";5�_�   L               M      /    ����                                                                                                                                                                                                                                                                                                                               /          N       v   N    d��w   H �         9      Ximport { FastApiDeleteAttachment } from "@/api/(site)/(blog)/posts/_components/service";5��