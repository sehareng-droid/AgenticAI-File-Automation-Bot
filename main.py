from groq import Groq
from dotenv import load_dotenv
import os
import logging

from logger_config import setup_logger
from read_content import read_content
from send_ai import send_ai
from PyPDF2 import PdfReader
import pandas as pd
import smtplib
from send_email import send_email

setup_logger()
logging.info('Application Started')
conversation_log = []

print("Type exit to quit, read_file to File read, send_email(send summaries via email) \
process folder(read all files via folder), history(to see conversation), clear to \
reset, save(save chat history)")

while True:
     intent= input("ask anything1: ").lower()
     

     if intent == "exit":
          print("program ended")
          break
     if intent == "read_file":
          folder_name= input("ask folder path: ")
          file_name = input("ask file name: ")
          
          try:
              path = os.path.join(folder_name,file_name)
              content= read_content(path)

          #Send file content to AI for summarization 
              ai_response = send_ai(content)
              
              print("\nAI Summary:\n")
              print(ai_response)
              
              conversation_log.append((file_name,ai_response))
              continue
              
          except Exception as e:
              print("Error calling API:", e)
              logging.error(str(e))


     # read all files via folder
     if intent == "process_folder":
          folder_name= input("ask folder path: ")
          try:
           content1 = []
           for file_name in os.listdir(folder_name):
              
          
             path = os.path.join(folder_name,file_name)
             content1.append(read_content(path))
          
          
           

          #Send file content to AI for summarization 
             full_content = "\n\n".join(content1)
             ai_response = send_ai(full_content)

            
    # Extract and print the AI's answer
            
             print(ai_response)
            
             conversation_log.append((f"Read file: {folder_name}",ai_response))
             continue
          except Exception as e:
              print("Error :", e)

              logging.error(str(e))
    
     
     if intent=="send_email":
          to_email=input("Enter email :")
          subject = input("enter subject :")
          
          if not conversation_log:
            print("No summary to send")
            continue

          body = conversation_log[-1][1]   # last AI response(last record ,second column)
          

          try:
           send_email(to_email, subject, body)
           print("Email sent successfully")
          except Exception as e:
           print("Email error:", e)
           logging.error(str(e))

          
            