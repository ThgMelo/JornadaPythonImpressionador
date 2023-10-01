import pyautogui
import time

# define o tempo de espera entre os comandos do PyAutoGUI
pyautogui.PAUSE = 0.5

# abrir google chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link do sistema que receberá os dados
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # como a internet pode estar lenta, o ideal é esperarmos um tempo para carregar o site



# Fazer login
pyautogui.click(x=765, y=461) # posições obtidas com auxilio do arquivo pegar_posicao.py
pyautogui.write("thiago@melo.com.br")
pyautogui.press("tab")
pyautogui.write("1a2b3c4d5e6f7g8")
pyautogui.press("enter")
time.sleep(3)



# importar os produtos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=745, y=309)
    # pegar da tabela o valor do campo que queremos preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))


    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim