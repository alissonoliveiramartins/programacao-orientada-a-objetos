with open('nomes.txt') as nome:
  with open('notas.txt') as nota:
    with open('troca_de_nota,txt', 'w')as saida:
      nome = list(nome)
      nota = list(nota)
      def troca(nome_inserido,nota_antiga,nota_nova):  
     
        cont= 0
        for posicao in nome:
          if  nome_inserido == posicao:
            break
          cont += 1

        cont1= 0
        for lugar in nota:
          if cont1 == cont:
            lugar= lugar.replace(nota_antiga,nota_nova)
          cont1 += 1
          return lugar
          
      print(troca('Kevin','8','0'))