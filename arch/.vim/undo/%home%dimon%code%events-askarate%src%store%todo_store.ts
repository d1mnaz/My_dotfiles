Vim�UnDo� �"s��r��B��]�pv2H���Iʵ��[�   R                revalidatePath('/');   M                          e�W    _�                             ����                                                                                                                                                                                                                                                                                                                                                             e�J    �         N    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e�J    �         O       �         O    5�_�                       +    ����                                                                                                                                                                                                                                                                                                                                                             e�K     �         O    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�]    �          O    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�^    �          P                  �          P    5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             e�_     �          P    5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             e�b    �          P      #                revalidatePath('/')5�_�      	                 $    ����                                                                                                                                                                                                                                                                                                                                                             e�b     �          P    5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             e�j    �                $                revalidatePath('/');5�_�   	              
   -       ����                                                                                                                                                                                                                                                                                                                                                             e�p    �   -   /   O    �   -   .   O    5�_�   
                 ?       ����                                                                                                                                                                                                                                                                                                                                                             e�v    �   ?   A   P    �   ?   @   P    5�_�                    L       ����                                                                                                                                                                                                                                                                                                                                                             e�z   	 �   L   N   Q    �   L   M   Q    5�_�                    M       ����                                                                                                                                                                                                                                                                                                                                                             e�}   
 �   -   N   2    �   -   .   R       $                revalidatePath('/');           } catch (error) {   9            console.error("Error creating todo:", error);   	        }       },   (    updateTodo: async (updatedTodo) => {           try {   L            const response = await fetch(`${URL}/todos/${updatedTodo.id}`, {                    method: "PATCH",                   headers: {   7                    "Content-Type": "application/json",                   },   2                body: JSON.stringify(updatedTodo),               });   6            const updatedItem = await response.json();               set((state) => ({   d                todos: state.todos.map((todo) => (todo.id === updatedItem.id ? updatedItem : todo)),               }));   $                revalidatePath('/');           } catch (error) {   9            console.error("Error updating todo:", error);   	        }       },       deleteTodo: async (id) => {           try {   /            await fetch(`${URL}/todos/${id}`, {   !                method: "DELETE",               });               set((state) => ({   D                todos: state.todos.filter((todo) => todo.id !== id),               }));   $                revalidatePath('/');5�_�                    @       ����                                                                                                                                                                                                                                                                                                                                                             e�J    �   ?   A   R                   revalidatePath('/');5�_�                    @       ����                                                                                                                                                                                                                                                                                                                                                             e�K    �   @   A   R    5�_�                    @   !    ����                                                                                                                                                                                                                                                                                                                                                             e�L     �   @   A   R    5�_�                    .       ����                                                                                                                                                                                                                                                                                                                                                             e�P    �   -   /   R                   revalidatePath('/');5�_�                    .       ����                                                                                                                                                                                                                                                                                                                                                             e�P    �   .   /   R    5�_�                    .   !    ����                                                                                                                                                                                                                                                                                                                                                             e�Q     �   .   /   R    5�_�                    M       ����                                                                                                                                                                                                                                                                                                                                                             e�V    �   L   N   R                   revalidatePath('/');5�_�                     M       ����                                                                                                                                                                                                                                                                                                                                                             e�V    �   M   N   R    5��