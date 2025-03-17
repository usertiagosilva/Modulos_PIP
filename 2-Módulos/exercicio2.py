import os

# # 1 - Desligar o computador 
# os.system("shutdown /s") # Desliga em 1 minuto
# os.system("shutdown /s /t 0") # Desliga imediatamente
# os.system("shutdown /r") # Reinicia em 1 minuto
# #os.system("shutdown now") - Linux

# # 2 - Cancelar o desligamento
# os.system("shutdown /a") # Cancela o desligamento

def turn_off_computer_in_one_hour():
    os.system("shutdown /s /t 3600") # Desliga em 1 hora
    
def turn_off_computer_in_half_hour():
    os.system("shutdown /s /t 1800") # Desliga em 30 minutos
    
def cancel_turn_off():
    os.system("shutdown /a") # Cancela o desligamento
      
turn_off_computer_in_one_hour()
cancel_turn_off()