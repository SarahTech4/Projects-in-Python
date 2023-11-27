# Criando uma calculadora em Python com interface!! 
from tkinter import * # -> Fazendo a importação do tkinter para criar interfaces :D (GOXTEI)
from tkinter import ttk

# Cores da nossa calculadora linda e maravilhosa
cor1 = '#1e1f1e' # preta
cor2 = '#feffff' # white/branco
cor3 = '#38576b' # azul carregado
cor4 = '#ECEFF1' # cizenta
cor5 = '#FFAB40' # orange/laranja

janela = Tk()
janela.eval('tk::PlaceWindow %s center' % janela.winfo_pathname(janela.winfo_id()))
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg= cor1)

frame_tela = Frame(janela, width=235, height=50, bg= cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#Variável todos os valores
todos_valores = ''

# Criando Label
valor_texto = StringVar()

#Criando Função
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    #passando valor para a tela
    valor_texto.set(todos_valores)


#Função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(resultado)

#função para limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set("")



app_label = Label(frame_tela, textvariable=valor_texto, width=15, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# Criando botões
b_1 = Button(frame_corpo, command= limpar_tela, text='C', width=11, height=2, bg= cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RAISED)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'),text='%', width=3, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text='/', width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text='8', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text='*', width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text='5', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text='-', width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text='+', width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text='.', width=3, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command = calcular, text='=', width=3, height=2, bg=cor4, font=('Ivy 13 bold'),relief=GROOVE, overrelief=GROOVE)
b_18.place(x=177, y=208)



janela.mainloop()
