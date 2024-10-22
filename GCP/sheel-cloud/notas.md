# Resumo sobre o Google Cloud Shell

O **Google Cloud Shell** é uma máquina virtual efêmera do Compute Engine que fornece um ambiente de linha de comando baseado em Linux, pré-configurado e gerenciado pelo Google. Ele permite interagir com os recursos do Google Cloud sem a necessidade de instalar ferramentas localmente.

## Características Principais

- **Instância Efêmera**: Cada sessão do Cloud Shell provisiona uma VM temporária que persiste enquanto a sessão está ativa. Após uma hora de inatividade, a sessão é encerrada e a VM é descartada.

- **Armazenamento Permanente**: Oferece **5 GB de armazenamento em disco permanente** montado no diretório `$HOME`. Esse armazenamento é persistente entre sessões, permitindo que arquivos, configurações e softwares instalados permaneçam salvos. Caso não seja acessado por **120 dias**, o diretório `$HOME` é excluído.

- **Ambiente Pré-configurado**: Vem com diversas ferramentas e linguagens pré-instaladas, incluindo:

  - **Ferramentas de CLI e Desenvolvimento**: Google Cloud CLI (`gcloud`), SDK do App Engine, Docker, Git, Maven, Gradle, entre outros.
  - **Suporte a Linguagens**:
    - **Java**: JRE/JDK 17.0.6 (OpenJDK)
    - **Go**: 1.20.4
    - **Python**: 3.9.2
    - **Node.js**: v18.12.1
    - **Ruby**: 2.7.8
    - **PHP**: 7.4.33
    - **.NET Core**: SDKs 2.1, 3.1, 5.0 e 6.0

- **Autorização Simplificada**: Ao realizar operações que exigem credenciais pela primeira vez, o Cloud Shell solicita autorização, facilitando o acesso aos recursos.

- **Variáveis de Ambiente Configuradas**: O projeto ativo no Console do Google Cloud é automaticamente definido no Cloud Shell, facilitando o uso imediato das ferramentas com o projeto correto.

## Funcionalidades Adicionais

- **Modo Temporário**: Permite iniciar o Cloud Shell sem o armazenamento permanente, resultando em tempos de inicialização mais rápidos. Contudo, dados não persistem entre sessões.

- **Modo de Segurança**: Caso haja problemas com arquivos de configuração (como `.bashrc`), é possível reiniciar o Cloud Shell em modo de segurança para corrigir esses arquivos.

- **Seleção de Região**: O Cloud Shell seleciona automaticamente a região mais próxima disponível. Não é possível escolher manualmente a região, mas o serviço tenta migrar para regiões mais próximas quando possível.

## Privilégios e Acesso

- **Usuário Root**: A conta fornecida possui privilégios de root, permitindo a execução de comandos `sudo` quando necessário.

## Atualizações e Manutenção

- **Atualizações Semanais**: A imagem do contêiner do Cloud Shell é atualizada semanalmente, garantindo acesso às versões mais recentes das ferramentas.

## Considerações Importantes

- **Limitações de Armazenamento**: Não é possível expandir o espaço de armazenamento além dos 5 GB fornecidos.

- **Persistência de Dados**: Para garantir que seus dados não sejam perdidos, mantenha backups regulares e acesse o Cloud Shell dentro de intervalos menores que 120 dias.

- **Personalização do Ambiente**: Embora seja possível instalar pacotes adicionais, instalações fora do diretório `$HOME` não persistirão após o término da instância. Considere usar scripts de personalização para automatizar a configuração do ambiente.

---

Este resumo fornece uma visão geral das principais funcionalidades e considerações ao utilizar o Google Cloud Shell, facilitando seu uso eficiente e seguro.
