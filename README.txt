Olá, professor! Espero que este arquivo tenha encontrado você em ótimo estado. A seguir, encontra-se algumas observações 
a respeito do que estou te entregando para atender a demanda do trabalho que você requisitou.

Primeiramente, gostaria de manifestar meus agradecimentos e admiração pelo curso oferecido por você neste semestre. Elogio teu
comprometimento com o curso, seja de forma síncrona ou assíncrona. O formato do curso certamente foi excepcional e de fato ofereceu
muitos aprendizados àqueles que se interessaram. Além disto, peço que não se desanime com a pouca adesão e a taxa de desistência no
curso, pois é válida a observação de que muitos estão muito mais interessados por suas matérias obrigatórias e a disciplina pode não
ter espaço na concorrência com as outras demandas do cotidiano dos estudantes.

Este trabalho certamente me ofereceu uma série de desafios e, consequentemente, uma série de aprendizados. Para a realização deste,
preferi que o relato deste estudo estivesse no formato de um texto contínuo, e por isso não encontrará as respostas separadas para
cada pergunta, apesar de que estão todas dentro do texto. O único cuidado nesta separação se revela na separação do texto por seções.

Durante o trabalho, preferi mexer com a linguagem de programação que sou mais familiarizado: o Python. Para os tipos de problemas
trabalhados nesse estudo encontra muito suporte dentro dessa linguagem, pois tem ampla utilização dentro da ciência de dados e da
própria programação científica.

Nesse sentido, para rodar os códigos aqui utilizados você precisa ter instalado o Python (versão 3.6 ou superior) e, também, as 
bibliotecas utilizadas: Numpy e o Matplotlib. Para instalação do Python, no Linux, dependerá da distribuição que você utiliza. 
Por exemplo, no Ubuntu/Debian, a instalação pode ser feita com o seguinte passo a passo:

# Atualize a lista de pacotes
sudo apt update

# Instale dependências
sudo apt install -y software-properties-common

# Adicione o repositório de Python mais atualizado (caso queira uma versão acima da disponível por padrão)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# Instale Python 3.10 (ou substitua por 3.6, 3.8, etc., se quiser outra versão)
sudo apt install -y python3.10 python3.10-venv python3.10-dev

# Verifique a instalação
python3.10 --version

No Fedora, a instalação pode ser feita da seguinte forma:

# Instale Python 3.10 (ou outra versão disponível)
sudo dnf install -y python3.10

# Verifique a instalação
python3.10 --version

Além desses dois métodos, existe um método universal com pyenv para instalação do python que é bastante útil quando você possui várias 
versões do python instalada, como por exemplo o python 2, que é muito comum:

# Instale dependências (válido para Ubuntu/Debian)
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Baixe e instale pyenv
curl https://pyenv.run | bash

# Adicione pyenv ao shell (bash)
echo -e '\n# Pyenv setup' >> ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Reinicie o shell ou execute:
exec "$SHELL"

# Instale uma versão do Python (ex: 3.10.12)
pyenv install 3.10.12

# Defina como padrão
pyenv global 3.10.12

# Verifique a instalação
python --version

Após a instalação do python, você deve também ter instalado as bibliotecas utilizadas nos códigos:

#Primeiro, verifique o python e o pip
python3.10 --version
python3.10 -m pip --version

#Se o pip não estiver instalado, use:
python3.10 -m ensurepip --upgrade

#OPCIONAL: Crie um diretório separado com os arquivos .py e os arquivos linha.dat e pontos.dat.
#Então, crie um ambiente virtual 
python3.10 -m venv meu_ambiente
source meu_ambiente/bin/activate

#Atualize o pip e depois instale as bibliotecas:
python3.10 -m pip install --upgrade pip
python3.10 -m pip install numpy matplotlib

#Se estiver num ambinte virtual, pode simplesmente fazer:
pip install --upgrade pip
pip install numpy matplotlib

#Se quiser instalar as bibliotecas para TODO o sistema, pode utilizar:
sudo python3.10 -m pip install numpy matplotlib

#Para executar os códigos python, verifique que você se encontra no diretório em que os arquivos se encontram e faça:
python3.10 [nome do arquivo].py

Qualquer dúvida, não hesite em me contatar.

Para a primeira parte do trabalho, vai encontrar dois códigos: ajuste_polinômio.py e ajuste_lagrange.py. O primeiro é uma tradução
70% fiel do código trabalhado com nossa classe, dentro de sala de aula, em fortran. As maiores alterações se encontram na construção
das matrizes envolvidas no sistema a ser resolvido com Gauss-Seidel, pois optei em substituir os laços de repetições utilizados para
estes fins por funções disponíveis pelo python que realizam as mesmas tarefas (como por exemplo: multiplicação de matrizes). Dessa forma,
valoriza-se melhor o método utilizado para resolução do problema.

Além deste código, temos o ajuste_lagrange.py. É fácil verificar que este código difere do anterior apenas no método utilizado para ajuste 
de polinômios, já que desta vez o método utilizado é a interpolação de Lagrange. A necessidade de buscar essa alternativa ainda na parte 1
veio de complicações numéricas advindas da complexidade adquirida pelo aumento de grau do polinômio, conforme relatado no relato do trabalho.

Para a segunda parte você vai encontrar o código splines.py, desenvolvido com base no método demonstrado também na parte 2 para splines cúbicas, 
e na terceira parte você tem o arquivo perceptron_de_rosenblatt.py, que também foi escrito encima da tradução do programa 7 disponível no moodle.
Certifique-se de que os arquivos estão no mesmo diretório que os arquivos .dat. 

No mais, muito obrigado por tudo!