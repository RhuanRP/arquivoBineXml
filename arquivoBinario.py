import pickle

def inserir_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o endereço de e-mail: ")

    contato = {"Nome": nome, "Telefone": telefone, "Email": email}
    return contato

def salvar_contatos(contatos):
    with open("C:/Users/Rhuan/Desktop/Faculdade e Estudos/Atividades 6° Periodo/Persistencia/N2/contatos.bin", "wb") as arquivo:
        pickle.dump(contatos, arquivo)
    print("Contato(s) salvo(s) com sucesso!")

def main():
    contatos = []
    while True:
        opcao = input("Digite '1' para inserir um contato ou '2' para sair: ")
        if opcao == '1':
            contato = inserir_contato()
            contatos.append(contato)
        elif opcao == '2':
            salvar_contatos(contatos)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
