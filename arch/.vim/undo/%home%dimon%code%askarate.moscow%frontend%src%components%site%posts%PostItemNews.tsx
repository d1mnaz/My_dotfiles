Vim�UnDo� ��+��tע~um�<gc(�z��Fu���{�"g3�   E   (        body: JSON.stringify(messageId),                             d�	    _�                             ����                                                                                                                                                                                                                                                                                                                                                  V        d�^    �             	   X            const endpoint = `${process.env.NEXT_PUBLIC_DOMAIN}/blogs/posts/${post.id}`;   #            await fetch(endpoint, {   !                method: "DELETE",                   headers: {   7                    "Content-Type": "application/json",   7                    "Access-Control-Allow-Origin": "*",                   },                   body: post.id,               });5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        d��    �         A    �         A    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       d��    �         E      6    const res = await fetch("/api/fastapi/messages", {5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       d��    �         E      *    await fetch("/api/fastapi/messages", {5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       d��    �         E      "    await fetch("/api/fastapi/", {�         E    5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                v       d��     �         E    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       d�     �         E      (        body: JSON.stringify(messageId),5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                v       d�     �         E              body: JSON.stringify(),�         E    5�_�      
           	      !    ����                                                                                                                                                                                                                                                                                                                                                v       d�    �         E    5�_�   	              
      "    ����                                                                                                                                                                                                                                                                                                                                                v       d�   	 �         E    5�_�   
                    $    ����                                                                                                                                                                                                                                                                                                                                                v       d�     �         E    5�_�                        #    ����                                                                                                                                                                                                                                                                                                                                                v       d�    �         A    �         E      '    await fetch("/api/fastapi/posts", {           method: "DELETE",   &        body: JSON.stringify(post.id),       });5��