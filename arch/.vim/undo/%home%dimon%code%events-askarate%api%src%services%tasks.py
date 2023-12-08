Vim�UnDo� �����,�s���7�� �ș�~��y�E�   $                                   e7    _�                             ����                                                                                                                                                                                                                                                                                                                                                             e�    �                   5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V        e6�    �                  'from schemas.tasks import TaskSchemaAdd�                /from utils.repository import AbstractRepository           class TasksService:   7    def __init__(self, tasks_repo: AbstractRepository):   :        self.tasks_repo: AbstractRepository = tasks_repo()       2    async def add_task(self, task: TaskSchemaAdd):   &        tasks_dict = task.model_dump()   ;        task_id = await self.tasks_repo.add_one(tasks_dict)           return task_id           async def get_tasks(self):   0        tasks = await self.tasks_repo.find_all()           return tasks5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V        e6�    �                   �               5�_�                    %       ����                                                                                                                                                                                                                                                                                                                            &                     V        e6�     �   %            5�_�                           ����                                                                                                                                                                                                                                                                                                                            &                     V        e6�    �   %               �       &       �               %   Mfrom schemas.tasks import TaskHistorySchemaAdd, TaskSchemaAdd, TaskSchemaEdit   /from utils.repository import AbstractRepository   (from utils.unitofwork import IUnitOfWork           class TasksService:   D    async def add_task(self, uow: IUnitOfWork, task: TaskSchemaAdd):   &        tasks_dict = task.model_dump()           async with uow:   9            task_id = await uow.tasks.add_one(tasks_dict)               await uow.commit()               return task_id       0    async def get_tasks(self, uow: IUnitOfWork):           async with uow:   .            tasks = await uow.tasks.find_all()               return tasks       T    async def edit_task(self, uow: IUnitOfWork, task_id: int, task: TaskSchemaEdit):   &        tasks_dict = task.model_dump()           async with uow:   9            await uow.tasks.edit_one(task_id, tasks_dict)       <            curr_task = await uow.tasks.find_one(id=task_id)   4            task_history_log = TaskHistorySchemaAdd(                    task_id=task_id,   ;                previous_assignee_id=curr_task.assignee_id,   0                new_assignee_id=task.assignee_id               )   <            task_history_log = task_history_log.model_dump()   <            await uow.task_history.add_one(task_history_log)               await uow.commit()       7    async def get_task_history(self, uow: IUnitOfWork):           async with uow:   7            history = await uow.task_history.find_all()               return history5�_�                             ����                                                                                                                                                                                                                                                                                                                            &          &           V        e7    �                /from utils.repository import AbstractRepository5��