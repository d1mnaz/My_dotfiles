Vim�UnDo� �Q/<���E��Z�"��=���d���?�V͎�   _       `                               e�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             e    �         Z       �         Y    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e     �         [    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e    �         [       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e     �         \    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e    �         \      from core.models import Base5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e    �         \      from .models import Base�         \    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e     �         \    5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             e    �                 from core.config import settings5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    eg    �         [      from src.models import Base5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    eg    �         [          �         [    5�_�   
                         ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    ei   	 �         [    5�_�                       I    ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    ei     �         `    5�_�                            ����                                                                                                                                                                                                                                                                                                                                         H       V   H    ep   
 �                config = context.config   Iconfig.set_main_option("sqlalchemy.url", "sqlite+aiosqlite:///sqlite.db")5�_�                            ����                                                                                                                                                                                                                                                                                                                                         H       V   H    er    �         ^    �         ^    5�_�                            ����                                                                                                                                                                                                                                                                                                                                         H       V   H    es    �                config = context.config5�_�                           ����                                                                                                                                                                                                                                                                                                                                         H       V   H    ev    �         _      from db.db import Base5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                         H       V   H    ex     �         _    5�_�                           ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e{    �         _      from models.tasks import Tasks5�_�                           ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e|    �         _    5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e}     �         _    5�_�                           ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e~    �         _      from models.users import Users5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e�     �         _    5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e�    �         _      "from src.models.tasks import Tasks5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e�    �         _      "from src.models.users import Users5�_�                           ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e�    �         _      target_metadata = None5�_�                           ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e�    �         _      target_metadata = �         _    5�_�                           ����                                                                                                                                                                                                                                                                                                                                         H       V   H    e�    �         _    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       e�    �                from src.db.db import Base   !from src.models.tasks import Task   !from src.models.users import User5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                V       e�    �   	      \    �   	   
   \    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       e�    �         _    5�_�                             ����                                                                                                                                                                                                                                                                                                                                                V       e�     �         `    5�_�                              ����                                                                                                                                                                                                                                                                                                                                                V       e�    �   _               �       `       �               `   import asyncio   %from logging.config import fileConfig       from sqlalchemy import pool   (from sqlalchemy.engine import Connection   ;from sqlalchemy.ext.asyncio import async_engine_from_config       from alembic import context       from src.db.db import Base   !from src.models.tasks import Task   !from src.models.users import User       3# this is the Alembic Config object, which provides   3# access to the values within the .ini file in use.   config = context.config   Iconfig.set_main_option("sqlalchemy.url", "sqlite+aiosqlite:///sqlite.db")       /# Interpret the config file for Python logging.   &# This line sets up loggers basically.   'if config.config_file_name is not None:   '    fileConfig(config.config_file_name)               '# add your model's MetaData object here   # for 'autogenerate' support   # from myapp import mymodel   )# target_metadata = mymodel.Base.metadata   target_metadata = Base.metadata       ?# other values from the config, defined by the needs of env.py,   # can be acquired:   E# my_important_option = config.get_main_option("my_important_option")   
# ... etc.           %def run_migrations_offline() -> None:   (    """Run migrations in 'offline' mode.       /    This configures the context with just a URL   5    and not an Engine, though an Engine is acceptable   2    here as well.  By skipping the Engine creation   /    we don't even need a DBAPI to be available.       @    Calls to context.execute() here emit the given string to the       script output.           """   2    url = config.get_main_option("sqlalchemy.url")       context.configure(           url=url,   (        target_metadata=target_metadata,           literal_binds=True,   -        dialect_opts={"paramstyle": "named"},       )       %    with context.begin_transaction():            context.run_migrations()           6def do_run_migrations(connection: Connection) -> None:   M    context.configure(connection=connection, target_metadata=target_metadata)       %    with context.begin_transaction():            context.run_migrations()           )async def run_async_migrations() -> None:   3    """In this scenario we need to create an Engine   0    and associate a connection with the context.           """       +    connectable = async_engine_from_config(   :        config.get_section(config.config_ini_section, {}),           prefix="sqlalchemy.",            poolclass=pool.NullPool,       )       3    async with connectable.connect() as connection:   4        await connection.run_sync(do_run_migrations)           await connectable.dispose()           $def run_migrations_online() -> None:   *    """Run migrations in 'online' mode."""       '    asyncio.run(run_async_migrations())           if context.is_offline_mode():       run_migrations_offline()   else:       run_migrations_online()5��