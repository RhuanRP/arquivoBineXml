import xml.etree.ElementTree as ET

def inserir_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o endereço de e-mail: ")

    contato = {"Nome": nome, "Telefone": telefone, "Email": email}
    return contato

def salvar_contatos_xml(contatos):
    root = ET.Element("Contatos")
    for contato in contatos:
        contato_elem = ET.SubElement(root, "Contato")
        nome_elem = ET.SubElement(contato_elem, "Nome")
        nome_elem.text = contato["Nome"]
        telefone_elem = ET.SubElement(contato_elem, "Telefone")
        telefone_elem.text = contato["Telefone"]
        email_elem = ET.SubElement(contato_elem, "Email")
        email_elem.text = contato["Email"]

    tree = ET.ElementTree(root)
    tree.write(r"C:/Users/Rhuan/Desktop/Faculdade e Estudos/Atividades 6° Periodo/Persistencia/N2/contatos.xml")
    print("Contato(s) salvo(s) em XML com sucesso!")

def ler_contatos_xml():
    try:
        tree = ET.parse("contatos.xml")
        root = tree.getroot()
        contatos = []
        for contato_elem in root.findall("Contato"):
            nome = contato_elem.find("Nome").text
            telefone = contato_elem.find("Telefone").text
            email = contato_elem.find("Email").text
            contato = {"Nome": nome, "Telefone": telefone, "Email": email}
            contatos.append(contato)
        return contatos
    except FileNotFoundError:
        return []

def main():
    contatos = ler_contatos_xml()
    while True:
        opcao = input("Digite '1' para inserir um contato, '2' para listar contatos ou '3' para sair: ")
        if opcao == '1':
            contato = inserir_contato()
            contatos.append(contato)
        elif opcao == '2':
            for i, contato in enumerate(contatos, start=1):
                print(f"Contato {i}:")
                print(f"Nome: {contato['Nome']}")
                print(f"Telefone: {contato['Telefone']}")
                print(f"E-mail: {contato['Email']}")
        elif opcao == '3':
            salvar_contatos_xml(contatos)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
