**Projeto Zoo: Simulação de um Zoológico Virtual**

O projeto Zoo é uma simulação de um zoológico virtual, desenvolvido em Python, que utiliza classes e métodos para gerenciar animais e recintos dentro do zoológico. O objetivo é criar um ambiente interativo onde os usuários podem criar, alimentar, brincar e gerenciar animais, além de cuidar dos recintos e atrair visitantes com base na felicidade dos animais.

**Classes Principais:**

1. **Animal:**
   - **Criar Animal:** Este método permite a criação de um novo animal no zoológico, especificando seu nome, espécie, nível de felicidade e nível de fome.
   - **Alimentar:** Ao alimentar um animal, seu nível de fome diminui e sua felicidade aumenta.
   - **Brincar:** Brincar com um animal aumenta sua felicidade, mas também o deixa com mais fome.

2. **Recinto:**
   - **Adicionar Animal:** Os animais criados são adicionados aos recintos, proporcionando um ambiente para sua interação.
   - **Remover Animal:** Permite a remoção de animais de um recinto específico.
   - **Listar Animais:** Mostra todos os animais presentes em um recinto.
   - **Limpar Recinto:** Remove todos os animais de um recinto, preparando-o para novas adições.
   - **Calcular Visitantes:** Com base na felicidade média dos animais em um recinto, o sistema calcula o número de visitantes atraídos para o zoológico.

**Estrutura do Projeto:**

- **zoo.py:** Este arquivo contém as definições das classes Animal e Recinto, juntamente com seus métodos e funcionalidades.
- **test_zoo.py:** É o arquivo de teste unitário, onde são realizados testes para garantir o funcionamento correto das funções em cada classe.
- **app.py:** O arquivo de aplicação principal, onde são testadas as principais funcionalidades do sistema como um todo, como criar animais, gerenciar recintos e atrair visitantes.

**Executando os Testes:**

Para executar os testes unitários, basta digitar "python test_zoo.py" no terminal. Isso garantirá que todas as funcionalidades individuais das classes sejam verificadas quanto à sua correta implementação.

Para testar o sistema como um todo e interagir com as principais funcionalidades, utilize "python app.py" no terminal. Isso permitirá uma experiência completa de gerenciamento do zoológico, desde a criação e cuidado dos animais até o monitoramento dos recintos e atração de visitantes com base na felicidade dos animais.

O projeto Zoo oferece uma oportunidade de aprendizado e diversão, explorando conceitos de programação orientada a objetos e simulação de ambientes interativos como um zoológico virtual.