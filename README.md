# Pet_ID

## Sobre o projeto

O **Pet_ID** é um projeto desenvolvido por **Igor de Abreu, Hugo Vieira e João Victor Funis** durante uma atividade relacionada ao **Kiro**, com o objetivo inicial de desenvolver uma solução de impacto social para ajudar na identificação e localização de pets perdidos.

A proposta nasceu durante o evento, mas não pôde ser finalizada dentro do período previsto devido a problemas técnicos e limitações do ambiente de desenvolvimento disponibilizado. Mesmo assim, a equipe decidiu continuar trabalhando na ideia posteriormente.

Durante essa continuação, percebemos que implementar toda a proposta original exigiria uma infraestrutura maior do que a necessária para um primeiro protótipo. Por isso, decidimos reformular o projeto e criar uma solução mais simples e direta, mantendo a essência da ideia: **facilitar a identificação de um pet encontrado e permitir o contato com seu tutor.**

## A ideia original

A proposta inicial era criar um sistema de identificação utilizando uma **coleira com QR Code**.

O funcionamento seria:

1. O tutor cadastraria as informações do pet.
2. Um QR Code seria gerado para aquele animal.
3. O QR Code seria colocado na coleira.
4. Caso o pet se perdesse e fosse encontrado por outra pessoa, ela poderia escanear o código utilizando um celular.
5. O código direcionaria para as informações de identificação do pet e de seu tutor.

As informações planejadas incluíam:

- Foto do pet;
- Nome do pet;
- Nome do tutor;
- Telefone;
- WhatsApp;
- E-mail.

A ideia também considerava uma arquitetura mais completa, com armazenamento centralizado das informações e uma página pública acessível através do QR Code.

## O que aconteceu durante o desenvolvimento

Durante o evento, a equipe encontrou problemas técnicos no ambiente disponibilizado para desenvolvimento, o que impediu que a implementação fosse concluída dentro do tempo previsto.

Em vez de abandonar completamente a proposta, decidimos continuar o projeto posteriormente e adaptar seu escopo.

Essa mudança também serviu como uma oportunidade para transformar a ideia inicial em um **MVP funcional**, reduzindo a complexidade e concentrando o desenvolvimento na funcionalidade principal.

## Versão atual

A versão presente neste repositório utiliza uma abordagem mais simples:

**Cadastro → geração do QR Code → identificação do pet**

O sistema permite realizar o cadastro das informações necessárias e gerar um QR Code associado aos dados do animal.

Ao acessar o endereço correspondente, é possível visualizar uma página de identificação do pet.

A implementação atual utiliza uma aplicação web em Python com Flask, além de bibliotecas para manipulação de imagens e geração de QR Codes.

## Tecnologias utilizadas

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **QRCode**
- **Pillow**

## Como executar

Clone o repositório:

```bash
git clone https://github.com/JV-Fox/Pet_ID.git
cd Pet_ID
```

Instale as dependências:

```bash
pip install pillow
pip install qrcode
pip install qrcode[pil]
pip install flask
```

Execute a aplicação:

```bash
python app.py
```

Após iniciar o servidor, será exibido no terminal um endereço semelhante a:

```text
http://127.0.0.1:5000
```

Abra esse endereço no navegador para acessar a página de cadastro.

Após concluir o cadastro, o sistema gera o QR Code e permite acessar a página de identificação do pet.

## Estrutura da ideia

```text
Tutor
  │
  ▼
Cadastro do pet
  │
  ├── Nome
  ├── Foto
  ├── Nome do tutor
  └── Contato
        │
        ▼
    Geração do QR Code
        │
        ▼
   Coleira do pet
        │
        ▼
  Pessoa encontra o animal
        │
        ▼
    Escaneia o QR Code
        │
        ▼
Página de identificação
        │
        ▼
Contato com o tutor
```

## Próximos passos

A versão atual é um protótipo e pode evoluir para uma solução mais completa.

Algumas possibilidades:

- Cadastro permanente dos pets;
- Banco de dados;
- URLs individuais para cada animal;
- Hospedagem em um servidor;
- Armazenamento das fotos;
- Geração de QR Codes permanentes;
- Edição das informações pelo tutor;
- Sistema de autenticação;
- Página otimizada para dispositivos móveis;
- Impressão de etiquetas ou cartões com o QR Code;
- Recursos para informar que um pet foi encontrado ou perdido.

## Sobre o Kiro

O desenvolvimento também serviu como uma experiência prática com o **Kiro** e com uma abordagem baseada em especificações.

A proposta original foi estruturada considerando:

**Requisitos → Design → Implementação**

Essa abordagem ajudou a equipe a transformar uma ideia inicial em uma estrutura mais concreta de desenvolvimento e também mostrou a importância de definir o escopo antes de implementar uma solução.

## Equipe

**Igor de Abreu**  
**Hugo Vieira**  
**João Victor Funis**

Projeto desenvolvido originalmente durante a atividade do Kiro e posteriormente continuado e reformulado pela equipe.

---

> **Pet_ID — uma ideia simples para aproximar pets encontrados de seus tutores.**
