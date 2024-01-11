# Бот написан для сервера бэкапера pg_probackup-15
# Powered by Maksim Kulikov, 2023

import telebot
from dotenv import load_dotenv
import os
import subprocess
import time
load_dotenv()

api = os.environ.get("API")
bot_name = os.environ.get("BOTNAME")
backuper = telebot.TeleBot(api)

# Получаем список комманд
@backuper.message_handler(func=lambda message: message.text.startswith('/help') or message.text.startswith(f'help@{bot_name}'))
def send_file(message):
   try:
       # Открываем файл для чтения
       with open('/home/backup_user/scripts/commands.txt', 'r') as file:
           # Читаем содержимое файла
           file_content = file.read()
       # Отправляем содержимое файла в чат
       backuper.send_message(message.chat.id, file_content)
   except FileNotFoundError:
       backuper.reply_to(message, 'Файл не найден')

### ВОССТАНОВЛЕНИЕ ###

#make restore_base ARG="" ARG2="" ARG3="" - восстановить определенную базу из бэкапа, где ARG="имя базы", ARG2="id бэкапа", ARG3="название инстанса"
@backuper.message_handler(func=lambda message: message.text.startswith('/restore_sql0') or message.text.startswith(f'restore_sql0@{bot_name}'))
def restore_base(message):
    try:
        arg1 = message.text.split()[1]
        arg2 = message.text.split()[2]
        subprocess.call(f'make restore_base ARG="{arg1}" ARG2="{arg2}" ARG3="db-sql0-pg15"', shell=True)
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/restore_sql1') or message.text.startswith(f'restore_sql1@{bot_name}'))
def restore_base(message):
    try:
        arg1 = message.text.split()[1]
        arg2 = message.text.split()[2]
        subprocess.call(f'make restore_base ARG="{arg1}" ARG2="{arg2}" ARG3="db-sql1-pg15"', shell=True)
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/restore_sql2') or message.text.startswith(f'restore_sql2@{bot_name}'))
def restore_base(message):
    try:
        arg1 = message.text.split()[1]
        arg2 = message.text.split()[2]
        subprocess.call(f'make restore_base ARG="{arg1}" ARG2="{arg2}" ARG3="db-sql2-pg15"', shell=True)
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/restore_sql3') or message.text.startswith(f'restore_sql3@{bot_name}'))
def restore_base(message):
    try:
        arg1 = message.text.split()[1]
        arg2 = message.text.split()[2]
        subprocess.call(f'make restore_base ARG="{arg1}" ARG2="{arg2}" ARG3="db-sql3-pg15"', shell=True)
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/restore_sql5') or message.text.startswith(f'restore_sql5@{bot_name}'))
def restore_base(message):
    try:
        arg1 = message.text.split()[1]
        arg2 = message.text.split()[2]
        subprocess.call(f'make restore_base ARG="{arg1}" ARG2="{arg2}" ARG3="db-sql5-pg15"', shell=True)
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')



### ПРОВЕРКА ИНСТАНСОВ ###

#make check_backups ARG3="" - показать все бэкапы, где ARG3="название инстанса"
@backuper.message_handler(func=lambda message: message.text.startswith('/show_sql0') or message.text.startswith(f'show_sql0@{bot_name}'))
def show_backups(message):
    try:
        output = subprocess.check_output(f'make check_backups ARG3="db-sql0-pg15"', shell=True)
        # декодируем в string
        output_str = output.decode('utf-8')
        # распределяем вывод по строкам
        lines = output_str.split('\n')
        # разрешаем выводить только определенное колическто строк
        short_output = '\n'.join(lines[:15])
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=short_output)
    except subprocess.CalledProcessError:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/show_sql1') or message.text.startswith(f'show_sql1@{bot_name}'))
def show_backups(message):
    try:
        output = subprocess.check_output(f'make check_backups ARG3="db-sql1-pg15"', shell=True)
        # декодируем в string
        output_str = output.decode('utf-8')
        # распределяем вывод по строкам
        lines = output_str.split('\n')
        # разрешаем выводить только определенное колическто строк
        short_output = '\n'.join(lines[:15])
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=short_output)
    except subprocess.CalledProcessError:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/show_sql2') or message.text.startswith(f'show_sql2@{bot_name}'))
def show_backups(message):
    try:
        output = subprocess.check_output(f'make check_backups ARG3="db-sql2-pg15"', shell=True)
        # декодируем в string
        output_str = output.decode('utf-8')
        # распределяем вывод по строкам
        lines = output_str.split('\n')
        # разрешаем выводить только определенное колическто строк
        short_output = '\n'.join(lines[:15])
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=short_output)
    except subprocess.CalledProcessError:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/show_sql3') or message.text.startswith(f'show_sql3@{bot_name}'))
def show_backups(message):
    try:
        output = subprocess.check_output(f'make check_backups ARG3="db-sql3-pg15"', shell=True)
        # декодируем в string
        output_str = output.decode('utf-8')
        # распределяем вывод по строкам
        lines = output_str.split('\n')
        # разрешаем выводить только определенное колическто строк
        short_output = '\n'.join(lines[:15])
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=short_output)
    except subprocess.CalledProcessError:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/show_sql5') or message.text.startswith(f'show_sql5@{bot_name}'))
def show_backups(message):
    try:
        output = subprocess.check_output(f'make check_backups ARG3="db-sql5-pg15"', shell=True)
        # декодируем в string
        output_str = output.decode('utf-8')
        # распределяем вывод по строкам
        lines = output_str.split('\n')
        # разрешаем выводить только определенное колическто строк
        short_output = '\n'.join(lines[:15])
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=short_output)
    except subprocess.CalledProcessError:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')


### ПРОВЕРКА БАЗ ###

@backuper.message_handler(func=lambda message: message.text.startswith('/show_db_sql0') or message.text.startswith(f'show_db_sql0@{bot_name}'))
def show_db_0(message):
  try:
      backuper.send_message(message.chat.id, 'запрос выполняется, пожалуйста подождите...')
      time.sleep(2)
      proc = subprocess.run(['bash', '/home/backup_user/scripts/get-database.sh','sql0-pg15'], capture_output=True, text=True)
      proc.check_returncode() # это вызовет CalledProcessError если скрипт не пройдет проверку

      # Используем rb - чтение бинарных данных, так как нужно передать файл
      with open('/home/backup_user/scripts/databases_sql0-pg15.txt', 'rb') as file:
          # Читаем содержимое файла
          file_content = file.read()

      # Отправляем файл в чат
      backuper.send_document(message.chat.id, file_content, caption='databases_sql0-pg15')
  except FileNotFoundError:
      backuper.reply_to(message, 'Файл не найден')
  except subprocess.CalledProcessError:
      backuper.reply_to(message, 'При выполнении команды произошла ошибка')
  except IndexError:
      backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/show_db_sql1') or message.text.startswith(f'show_db_sql1@{bot_name}'))
def show_db_1(message):
  try:
      backuper.send_message(message.chat.id, 'запрос выполняется, пожалуйста подождите...')
      time.sleep(2)
      proc = subprocess.run(['bash', '/home/backup_user/scripts/get-database.sh','sql1-pg15'], capture_output=True, text=True)
      proc.check_returncode() # это вызовет CalledProcessError если скрипт не пройдет проверку

      # Используем rb - чтение бинарных данных, так как нужно передать файл
      with open('/home/backup_user/scripts/databases_sql1-pg15.txt', 'rb') as file:
          # Читаем содержимое файла
          file_content = file.read()

      # Отправляем файл в чат
      backuper.send_document(message.chat.id, file_content, caption='databases_sql1-pg15')
  except FileNotFoundError:
      backuper.reply_to(message, 'Файл не найден')
  except subprocess.CalledProcessError:
      backuper.reply_to(message, 'При выполнении команды произошла ошибка')
  except IndexError:
      backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/show_db_sql2') or message.text.startswith(f'show_db_sql2@{bot_name}'))
def show_db_2(message):
  try:
      backuper.send_message(message.chat.id, 'запрос выполняется, пожалуйста подождите...')
      time.sleep(2)
      proc = subprocess.run(['bash', '/home/backup_user/scripts/get-database.sh','sql2-pg15'], capture_output=True, text=True)
      proc.check_returncode() # это вызовет CalledProcessError если скрипт не пройдет проверку

      # Используем rb - чтение бинарных данных, так как нужно передать файл
      with open('/home/backup_user/scripts/databases_sql2-pg15.txt', 'rb') as file:
          # Читаем содержимое файла
          file_content = file.read()

      # Отправляем файл в чат
      backuper.send_document(message.chat.id, file_content, caption='databases_sql2-pg15')
  except FileNotFoundError:
      backuper.reply_to(message, 'Файл не найден')
  except subprocess.CalledProcessError:
      backuper.reply_to(message, 'При выполнении команды произошла ошибка')
  except IndexError:
      backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/show_db_sql3') or message.text.startswith(f'show_db_sql3@{bot_name}'))
def show_db_3(message):
  try:
      backuper.send_message(message.chat.id, 'запрос выполняется, пожалуйста подождите...')
      time.sleep(2)
      proc = subprocess.run(['bash', '/home/backup_user/scripts/get-database.sh','sql3-pg15'], capture_output=True, text=True)
      proc.check_returncode() # это вызовет CalledProcessError если скрипт не пройдет проверку

      # Используем rb - чтение бинарных данных, так как нужно передать файл
      with open('/home/backup_user/scripts/databases_sql3-pg15.txt', 'rb') as file:
          # Читаем содержимое файла
          file_content = file.read()

      # Отправляем файл в чат
      backuper.send_document(message.chat.id, file_content, caption='databases_sql3-pg15')
  except FileNotFoundError:
      backuper.reply_to(message, 'Файл не найден')
  except subprocess.CalledProcessError:
      backuper.reply_to(message, 'При выполнении команды произошла ошибка')
  except IndexError:
      backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/show_db_sql5') or message.text.startswith(f'show_db_sql5@{bot_name}'))
def show_db_1(message):
  try:
      backuper.send_message(message.chat.id, 'запрос выполняется, пожалуйста подождите...')
      time.sleep(2)
      proc = subprocess.run(['bash', '/home/backup_user/scripts/get-database.sh','sql5-pg15'], capture_output=True, text=True)
      proc.check_returncode() # это вызовет CalledProcessError если скрипт не пройдет проверку

      # Используем rb - чтение бинарных данных, так как нужно передать файл
      with open('/home/backup_user/scripts/databases_sql5-pg15.txt', 'rb') as file:
          # Читаем содержимое файла
          file_content = file.read()

      # Отправляем файл в чат
      backuper.send_document(message.chat.id, file_content, caption='databases_sql5-pg15')
  except FileNotFoundError:
      backuper.reply_to(message, 'Файл не найден')
  except subprocess.CalledProcessError:
      backuper.reply_to(message, 'При выполнении команды произошла ошибка')
  except IndexError:
      backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')



'''
@backuper.message_handler(func=lambda message: message.text.startswith('/show_db_sql0') or message.text.startswith(f'show_db_sql0@{bot_name}'))
def show_db_0(message):
  try:
      backuper.send_message(message.chat.id, 'запрос выполняется, пожалуйста подождите...')
      time.sleep(2)
      proc = subprocess.run(['bash', '/home/backup_user/scripts/get-database.sh','sql0-pg15'], capture_output=True, text=True)
      proc.check_returncode() # это вызовет CalledProcessError если скрипт не пройдет проверку

      # Открываем файл для чтения
      with open('/home/backup_user/scripts/databases_sql0-pg15.txt', 'r') as file:
          # Читаем содержимое файла
          file_content = file.read()

      # Разбиваем содержимое файла на части по 4096 символов
      parts = [file_content[i:i+4096] for i in range(0, len(file_content), 4096)]

      # Отправляем каждую часть содержимого файла в чат
      for part in parts:
          backuper.send_message(message.chat.id, part)
  except FileNotFoundError:
      backuper.reply_to(message, 'Файл не найден')
  except subprocess.CalledProcessError:
      backuper.reply_to(message, 'При выполнении команды произошла ошибка')
  except IndexError:
      backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')
'''


# Проверка WAL
@backuper.message_handler(func=lambda message: message.text.startswith('/show_wal') or message.text.startswith(f'show_wal@{bot_name}'))
def show_wal(message):
    try:
        backuper.send_message(message.chat.id, 'запрос выполняется, пожалуйста подождите...')
        time.sleep(2)
        output = subprocess.check_output(f'make check_wal', shell=True)
        # декодируем в string
        output_str = output.decode('utf-8')
        # распределяем вывод по строкам
        lines = output_str.split('\n')
        # разрешаем выводить только определенное колическто строк
        short_output = '\n'.join(lines[:20])
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=short_output)
    except subprocess.CalledProcessError:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')        

@backuper.message_handler(func=lambda message: message.text.startswith('/freespace') or message.text.startswith(f'freespace@{bot_name}'))
def show_space(message):
    try:
        output = subprocess.check_output(f'df -h', shell=True)
        # декодируем в string
        output_str = output.decode('utf-8')
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=output_str)
    except subprocess.CalledProcessError:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

@backuper.message_handler(func=lambda message: message.text.startswith('/status') or message.text.startswith(f'status@{bot_name}'))
def show_errors(message):
    try:
        backuper.send_message(message.chat.id, 'запрос выполняется, пожалуйста подождите...')
        time.sleep(2)
        proc = subprocess.run(['bash', '/home/backup_user/scripts/status.sh'], capture_output=True, text=True)
        proc.check_returncode()  # это вызовет CalledProcessError если скрипт не пройдет проверку
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=proc.stdout)
    except subprocess.CalledProcessError as err:
        backuper.reply_to(message, f'При выполнении команды произошла ошибка: {err.output}')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

# Изменение данных в crontab

@backuper.message_handler(func=lambda message: message.text.startswith('/show_crontab') or message.text.startswith(f'show_crontab@{bot_name}'))
def show_crontab(message):
    try:
        output = subprocess.check_output(f'crontab -l', shell=True)
        # декодируем в string
        output_str = output.decode('utf-8')
        # Отправляем вывод команды, как сообщение
        backuper.send_message(chat_id=message.chat.id, text=output_str)
    except subprocess.CalledProcessError:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка')
    except IndexError:
        backuper.reply_to(message, 'Недопустимое использование команды. Пожалуйста, укажите правильную команду бота')

# Создаем словарь для хранения состояния каждого чата
chat_states = {}

@backuper.message_handler(func=lambda message: message.text.startswith('/change_crontab') or message.text.startswith(f'change_crontab@{bot_name}'))
def change_crontab(message):
  # Устанавливаем состояние чата в "waiting_for_task"
  chat_states[message.chat.id] = "waiting_for_task"
  backuper.send_message(message.chat.id, 'Внимание, вы пытаетесь изменить задачи крон, все текущие задачи будут удалены! Для отмены данного действия введите /cancel')
  time.sleep(1)
  backuper.send_message(message.chat.id, 'Введите список задач')

@backuper.message_handler(func=lambda message: message.text.startswith('/cancel') or message.text.startswith(f'cancel@{bot_name}'))
def cancel(message):
    try:
        if message.chat.id in chat_states:
            del chat_states[message.chat.id]
            backuper.send_message(message.chat.id, 'Отмена выполнения команды')
        else:
            backuper.send_message(message.chat.id, 'Отмена невозможна. Команда не выполняется')
    except Exception as e:
        backuper.reply_to(message, 'При выполнении команды произошла ошибка: {}'.format(e))

@backuper.message_handler(func=lambda message: chat_states.get(message.chat.id) == "waiting_for_task")
def receive_task(message):
  try:
      # Удаляем старые задачи
      subprocess.run(["crontab", "-r"])
      # Изменяем crontab
      subprocess.call(f'(crontab -l ; echo "{message.text}") | crontab -', shell=True)
      backuper.send_message(message.chat.id, 'Crontab успешно изменен')
  except subprocess.CalledProcessError:
      backuper.reply_to(message, 'Произошла ошибка при изменении crontab')
  finally:
      # Удаляем состояние чата
      del chat_states[message.chat.id]

backuper.polling()

