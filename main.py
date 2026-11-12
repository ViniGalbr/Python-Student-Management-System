alunos = []

def adicionar_aluno():
    while True:
            nome = input('write the student name:\n')
            if not nome:
                print('Student name cannot be empty!')
            else:
                break
    
    while True:
        try:
            idade = int(input('Enter your age:\n'))
            if idade < 0:
                print("The age cannot be under 0, insert a valid age.")
            else:
                break

            
        except ValueError:
            print('Invalid age! Please enter a number.')
    
    while True:
        try:
            nota = float(input('grade of the student:\n'))
            if nota <0 or nota >10:
                print('invalid grade, must be a number between 0 and 10')
            else:
                print('student added succesfully!')
                break
        except ValueError:
            print("Invalid grade, enter a number.")
    
    aluno = {
        'nome' : nome,
        'idade' : idade,
        'nota' : nota
    }
    return aluno

def buscar_aluno():
    pessoa = input('insert a name:\n').strip()
    return pessoa

while True:
    try:
        option = int(input('1.add a student:\n2.list all the students:\n3.search an student:\n4.remove a student:\n5.show the GPA:\n6.exit\n'))
    except ValueError:
        print('select a valid option number!')
        continue
    
    match option:
        case 1:
            salvar_aluno = adicionar_aluno()
            if salvar_aluno is not None:
                alunos.append(salvar_aluno)
        case 2:
            for aluno in alunos:
                print(f"nome: {aluno['nome']}")
                print(f"idade: {aluno['idade']}")
                print(f"nota: {aluno['nota']}")
                print('='*30)
            if not alunos:
                print('there are no registered students')
        case 3:
            pessoa = buscar_aluno()
            encontrado = False
            
            for aluno in alunos:
                if aluno['nome'].lower() == pessoa.lower():
                    print(f"nome: {aluno['nome']}")
                    print(f"idade: {aluno['idade']}")
                    print(f"nota: {aluno['nota']}")
                    
                    encontrado = True
                    break
                
            if not encontrado:
                print('student not found')
        case 4:
            pessoa = buscar_aluno()
            encontrado = False
            
            for aluno in alunos:
                if aluno['nome'].lower() == pessoa.lower():
                    encontrado = True
                    alunos.remove(aluno)
                    print('student removed succesfully!')
                    break
            if not encontrado:
                print('student not found!')
        case 5:
            soma = 0
            for aluno in alunos:
                soma += float(aluno['nota'])
                
            if alunos:
                resultado = soma / len(alunos)
                print(f"average grade is {resultado:.2f}")
            else:
                print('no student registered!')
                
        case 6:
            print('goodbye')
            break    
        
        case _:
            print('select a option between 1 and 6.')
            continue