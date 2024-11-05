### Introdução a Configuração de Projetos no GCP

No Google Cloud Platform (GCP), **projetos** são a unidade organizacional básica para agrupar e gerenciar recursos. Configurar corretamente os projetos é essencial para garantir uma gestão eficiente de recursos e facilitar a administração de custos e acessos.

---

### Termos e Definições:

1. **Organização**:
   - Representa a entidade principal que agrupa todos os projetos e recursos de uma empresa ou organização. 
   - **Exemplo**: Uma empresa com várias equipes e projetos pode usar a organização como nível mais alto de administração.

2. **Folders (Pastas)**:
   - Pastas são usadas para organizar projetos e outros recursos dentro da hierarquia da organização.
   - **Uso**: Facilita a separação por equipes, departamentos ou ambientes (ex: produção, teste).

3. **Resource (Recursos)**:
   - São todos os componentes que podem ser utilizados em um projeto no GCP, como VMs, buckets de armazenamento e bancos de dados.
   - **Exemplo**: Um bucket no Cloud Storage é um recurso dentro de um projeto.

4. **Projetos**:
   - Cada projeto é um container de recursos e tem um identificador exclusivo. Todo recurso deve pertencer a um projeto.
   - **Uso**: Agrupar recursos relacionados a uma aplicação ou serviço.

5. **API**:
   - APIs são ativadas por projeto para permitir que recursos se comuniquem e realizem operações específicas.
   - **Uso**: Ativar a API do Compute Engine para rodar VMs dentro de um projeto.

6. **Service Account (Conta de Serviço)**:
   - Contas de serviço são identidades associadas a aplicações ou serviços para interagir com outros recursos do GCP.
   - **Uso**: Um aplicativo pode usar uma conta de serviço para acessar dados em um bucket do Cloud Storage.

7. **Super Admin**:
   - O administrador principal que tem controle total sobre a organização e os projetos.
   - **Uso**: Gerenciar configurações globais, como controle de acesso e administração de contas de faturamento.

8. **IAM (Identity and Access Management)**:
   - Ferramenta para controle de acesso, permitindo gerenciar quem pode acessar quais recursos e com quais permissões.
   - **Exemplo**: Atribuir o papel de “Viewer” a um membro que só pode visualizar recursos.

9. **ROLE (Papéis)**:
   - Papéis são conjuntos de permissões atribuídos a usuários ou contas de serviço.
   - **Exemplo**: O papel de “Storage Admin” permite gerenciar buckets e objetos no Cloud Storage.

10. **Identities (Identidades)**:
   - Refere-se às entidades que interagem com os recursos, como usuários, grupos ou contas de serviço.
   - **Uso**: Uma conta de serviço atua como identidade para um aplicativo que acessa recursos do GCP.

11. **Billing Account (Conta de Cobrança)**:
   - Conta associada aos projetos para registrar custos e gerenciar pagamentos.
   - **Uso**: Cada projeto deve estar vinculado a uma conta de cobrança ativa para consumir recursos pagos.

---

### Projetos e Contas

- **Projetos e Contas** são vinculados diretamente à estrutura organizacional do GCP. A configuração de projetos é essencial para garantir controle sobre os recursos e facilitar a administração de custos e acessos.
- A vinculação correta entre **projetos** e **contas de cobrança** garante uma gestão financeira clara e evita interrupções no uso de serviços.

---

Com uma configuração clara de projetos, pastas e contas, é possível gerenciar recursos, segurança e custos de forma eficiente no GCP. A correta organização de pastas e a ativação das APIs necessárias garantem um fluxo de trabalho otimizado e seguro.

### Projetos e Contas no GCP

No Google Cloud Platform (GCP), **projetos e contas** são elementos fundamentais para organizar, gerenciar e controlar os recursos e custos na nuvem. Cada projeto precisa estar vinculado a uma **conta de cobrança** para consumir serviços pagos, garantindo uma gestão eficiente e transparente.

---

### Estrutura de Projetos no GCP

1. **Projetos**:
   - Cada projeto é um container que agrupa e organiza recursos, como VMs, buckets e bancos de dados.
   - **Identificação**: Cada projeto tem um **ID único**, um **nome** e um **número de projeto**.
   - **Vinculação**: Todo recurso no GCP pertence a um projeto específico, o que facilita a separação e controle de diferentes workloads.
   - **Uso**: Um projeto pode ser criado para cada aplicação, equipe ou ambiente (como teste e produção).
   - **Exemplo**: Um projeto pode ser usado para hospedar um site e outro para um sistema de processamento de dados.

2. **Recursos dentro de Projetos**:
   - Recursos são todos os elementos que uma aplicação pode usar, como máquinas virtuais, bancos de dados ou buckets de armazenamento.
   - **Importante**: A desativação ou exclusão de um projeto desativa automaticamente todos os recursos associados a ele.

---

### Contas de Cobrança

1. **Billing Account (Conta de Cobrança)**:
   - Uma **conta de cobrança** é necessária para ativar recursos pagos no GCP.
   - Pode ser vinculada a um ou mais projetos, e os custos são cobrados com base no uso dos recursos desses projetos.

2. **Tipos de Contas**:
   - **Contas pré-pagas**: Requer pagamento antecipado dos serviços.
   - **Contas pós-pagas**: Os custos são faturados mensalmente de acordo com o uso.

3. **Vinculação entre Projeto e Conta**:
   - Um projeto deve estar **vinculado a uma conta de cobrança ativa** para consumir serviços pagos.
   - **Exemplo**: Um projeto pode estar vinculado a uma conta de cobrança específica da empresa para consolidar todos os custos de serviços em um único pagamento.

4. **Organização de Custos**:
   - Usar **etiquetas e pastas** nos projetos facilita a identificação e alocação de custos para diferentes equipes ou serviços.
   - **Exemplo**: Etiquetar projetos por cliente ou por ambiente (produção, teste) para rastrear despesas facilmente.

---

### Importância da Gestão de Projetos e Contas

- **Segurança e Controle**: A vinculação de projetos e contas permite monitorar o uso e controlar o acesso a recursos críticos.
- **Transparência Financeira**: Consolidar projetos sob uma mesma conta de cobrança facilita a análise de custos e previsão orçamentária.
- **Escalabilidade**: A estrutura modular do GCP permite adicionar ou remover projetos facilmente, sem impactar outros projetos ou recursos.

---

### Exemplos Práticos de Uso

- **Projeto para cada ambiente**: Uma empresa pode criar projetos separados para os ambientes de desenvolvimento, teste e produção.
- **Projeto por cliente ou produto**: Para agências ou consultorias, é possível criar um projeto separado para cada cliente, facilitando a gestão financeira e o controle de recursos.
- **Contas de cobrança separadas**: Diferentes unidades de negócios podem ter contas de cobrança separadas para organizar e controlar melhor os custos.

---

A correta configuração de **projetos e contas** no GCP garante uma administração eficiente de recursos e custos, permitindo que as organizações escalem seus serviços com segurança e previsibilidade financeira.

### Detalhes Importantes sobre Projetos e Contas no GCP

1. **Todo Projeto faz parte de uma Estrutura Organizacional**:
   - No GCP, todos os projetos estão vinculados a uma **estrutura organizacional**, o que facilita o gerenciamento centralizado de recursos, contas de cobrança e políticas de acesso.
   - **Organização** é a entidade principal que agrupa todos os projetos e recursos.

2. **Um Projeto só pode ter uma Organização Associada**:
   - Cada projeto pode estar vinculado a apenas **uma organização**.
   - **Importante**: Uma vez que o projeto é associado a uma organização, ele não pode ser movido para outra.

3. **Uso de Folders (Pastas) para Organização**:
   - As **pastas** ajudam a organizar projetos e recursos, especialmente em ambientes com muitos serviços e equipes.
   - **Exemplo**: Uma empresa pode criar pastas para diferentes departamentos, como TI, Marketing e RH, ou separar ambientes por produção, teste e desenvolvimento.

4. **Permissões Hereditárias**:
   - As **permissões** podem ser herdadas ao longo da hierarquia da organização, ou seja, permissões atribuídas a uma organização ou pasta são propagadas para os projetos e recursos contidos nela.
   - **Exemplo**: Se um grupo tiver acesso de "Visualizador" na pasta "TI", ele automaticamente terá acesso aos projetos contidos nessa pasta.

5. **Permissões Adicionais para Herdeiros**:
   - Embora as permissões sejam herdadas, **é possível conceder permissões adicionais** em níveis inferiores.
   - **Exemplo**: Um membro pode herdar acesso de "Visualizador" de uma pasta, mas ter também a função de "Editor" em um projeto específico dentro dessa pasta.

---

### Resumo da Hierarquia de Projetos e Contas

- **Organização**: Entidade principal que agrupa todos os recursos e projetos.
- **Folders (Pastas)**: Facilitam a organização por departamentos, equipes ou ambientes.
- **Projetos**: Contêm recursos e são vinculados a uma única organização.
- **Permissões**: Podem ser herdadas ao longo da hierarquia, mas podem ser personalizadas com permissões adicionais em níveis inferiores.

---

Com uma estrutura bem planejada usando **organizações**, **pastas** e **projetos**, é possível administrar de forma eficiente os recursos do GCP. O uso de permissões herdadas e específicas garante flexibilidade e segurança no controle de acessos.

# Hierarquia entre Projetos, Organizações, Pastas e Subpastas no GCP

No **Google Cloud Platform (GCP)**, a hierarquia de recursos é essencial para gerenciar de forma eficaz o acesso, as políticas e o faturamento dos recursos em nuvem. A hierarquia é estruturada em **quatro níveis principais**:

1. **Organização**  
2. **Pastas**  
3. **Projetos**  
4. **Recursos**

---

## 1. Organização

- **Nível mais alto** na hierarquia.
- Representa a empresa ou entidade que está utilizando o GCP.
- Permite aplicar políticas e permissões que se propagam para todos os recursos abaixo.
- **Exemplo:** `minha-empresa.com`

---

## 2. Pastas

- **Opcional**, mas útil para estruturar recursos de forma lógica.
- Podem conter outras pastas ou projetos.
- Facilitam a aplicação de políticas em grupos específicos de recursos.
- **Exemplo:** `Departamento de TI`, `Equipe de Desenvolvimento`

---

## 3. Projetos

- **Unidade principal de organização** para recursos.
- Todos os recursos no GCP pertencem a um projeto.
- Isolam recursos, políticas e permissões.
- **Exemplo:** `projeto-site-web`, `projeto-app-mobile`

---

## 4. Recursos

- **Entidades individuais** como VMs, bancos de dados, buckets de armazenamento, etc.
- Herdam políticas e permissões dos níveis superiores.
- **Exemplo:** Instância Compute Engine, Bucket Cloud Storage

---

## Visão Geral da Hierarquia

Organização └── Pasta ├── Subpasta │ └── Projeto │ └── Recursos └── Projeto └── Recursos

### Roles e Permissões no Google Cloud Platform (GCP)

No GCP, **roles** e **permissões** são componentes-chave para o gerenciamento de acesso e segurança de recursos. O controle de acesso é baseado em Identidade e Gerenciamento de Acesso (IAM), onde **permissões** definem ações específicas que uma entidade (como um usuário ou serviço) pode realizar em um recurso (como um bucket de armazenamento). As permissões são agrupadas em **roles** (papéis), que podem ser atribuídos a usuários, grupos ou contas de serviço.

#### Tipos de Roles:
1. **Primitive Roles**: Incluem "Owner", "Editor" e "Viewer" e concedem permissões gerais.
2. **Predefined Roles**: São roles com permissões específicas para serviços, como `Storage Admin` ou `Compute Viewer`.
3. **Custom Roles**: Criados para necessidades específicas, permitindo granularidade nas permissões atribuídas.

#### Exemplos:
- **Viewer**: Pode visualizar recursos mas não pode alterá-los.
- **Editor**: Pode criar e modificar recursos, mas não tem controle total.
- **Owner**: Tem controle total, incluindo a possibilidade de gerenciar permissões.

Ao configurar roles e permissões, é recomendável aplicar o princípio do menor privilégio, garantindo que usuários ou serviços tenham apenas as permissões estritamente necessárias para desempenhar suas funções.

### Contas de Serviço no Google Cloud Platform (GCP)

No GCP, **contas de serviço** são uma forma de identidade usada para autorizar aplicações e serviços a interagir com outros recursos na plataforma com segurança. Elas permitem que aplicações autenticadas façam chamadas à API e acessem recursos, sem a necessidade de usar credenciais de usuário. Além de segurança e controle de acesso, contas de serviço podem impactar o **Billing (faturamento)**, pois elas gerenciam o uso e as permissões sobre recursos que geram custos.

#### Características das Contas de Serviço:
- **Credenciais**: Cada conta de serviço possui credenciais específicas (geralmente em formato de chave JSON) para autenticar e autorizar ações.
- **Roles e Permissões**: Atribuir roles específicas permite definir o que cada conta de serviço pode fazer. Por exemplo, uma conta de serviço com o role `BigQuery User` pode ler e escrever dados no BigQuery.
- **Uso de IAM**: Contas de serviço são gerenciadas pelo Identity and Access Management (IAM), que permite controlá-las como qualquer outra identidade de usuário, com permissões detalhadas.

#### Billing e Contas de Serviço:
Toda ação executada por uma conta de serviço que consome recursos do GCP (como armazenamento, processamento de dados ou execução de VMs) gera **custos** associados ao projeto em que a conta está registrada. Portanto, é essencial gerenciar roles para limitar ações desnecessárias e evitar custos adicionais. Em muitos casos, é recomendável monitorar as atividades de contas de serviço que utilizam APIs que possuem custos variáveis para evitar cobranças inesperadas.

#### Principais Tipos de Contas de Serviço:
1. **Contas de Serviço do Usuário**: Criadas por um usuário para uma aplicação específica, permitindo controle total sobre permissões. Esse tipo é o mais comum.
2. **Contas de Serviço Gerenciadas pelo Google**: Usadas internamente para operar serviços do GCP, como Compute Engine e App Engine. Essas contas geralmente têm permissões específicas de acordo com o serviço.
3. **Contas de Serviço Padrão**: Criadas automaticamente quando certos recursos são implementados, como VMs no Compute Engine. Elas podem ter permissões pré-definidas e devem ser revisadas conforme necessário.

#### Exemplo Prático: Configurando uma Conta de Serviço para BigQuery
Imagine que você tem uma aplicação que precisa ler dados do BigQuery. Para evitar custos adicionais, você pode criar uma conta de serviço com permissões mínimas para essa tarefa:

1. No **Console do GCP**, vá para **IAM & Admin > Service Accounts**.
2. Clique em **Create Service Account** e defina um nome e ID.
3. Atribua o role `BigQuery Data Viewer` para garantir que a conta possa apenas visualizar os dados.
4. Gere uma chave JSON para a conta de serviço, se a aplicação precisar de autenticação fora do ambiente do GCP.

Esse controle de permissões reduz os riscos de ações não intencionais que possam gerar custos adicionais e promove segurança.

### Alertas de Cobranças no Google Cloud Platform (GCP)

Os alertas de cobranças no GCP ajudam a monitorar gastos e evitar surpresas na fatura. É possível configurar **alertas de orçamento** que notificam quando um limite de gastos definido é atingido. Estes alertas podem ser configurados pelo Console do GCP em **Billing > Budgets & alerts** e enviados por e-mail, ajudando a acompanhar os custos em tempo real e ajustá-los conforme necessário.

**Passos rápidos para configurar:**
1. Vá para **Billing > Budgets & alerts**.
2. Defina um orçamento e os valores de alerta (ex.: 50%, 90%, 100% do orçamento).
3. Ative as notificações por e-mail.

Esses alertas são fundamentais para controlar o uso dos recursos e evitar gastos excessivos.

### Cloud Functions no Google Cloud Platform (GCP)

**Cloud Functions** é um serviço de computação serverless no GCP que permite executar código em resposta a eventos sem a necessidade de gerenciar infraestrutura. As **Functions** são ideais para tarefas de pequena escala que respondem a eventos, como processamento de arquivos, webhooks, integrações com APIs e manipulação de dados.

#### Características Principais:
- **Totalmente Gerenciado**: O GCP lida com o provisionamento, o escalonamento e a manutenção da infraestrutura.
- **Trigger por Eventos**: As funções podem ser disparadas por eventos do GCP (como modificações em buckets do Cloud Storage, mensagens do Pub/Sub) ou chamadas HTTP.
- **Escalonamento Automático**: Cloud Functions escalam automaticamente com base na demanda.

#### Exemplo de Uso: Integrar Cloud Functions com uma API
É comum usar Cloud Functions para construir APIs, processar dados em tempo real ou responder a eventos específicos, como uploads de arquivos ou mensagens em filas.

#### Como Criar uma Cloud Function:
1. No **Console do GCP**, vá para **Cloud Functions** e clique em **Create Function**.
2. Escolha um gatilho (HTTP ou baseado em eventos).
3. Escreva seu código ou faça upload.
4. Configure permissões e clique em **Deploy**.

Cloud Functions são cobradas por tempo de execução e recursos utilizados, o que torna importante o controle sobre a quantidade de chamadas e o tempo de execução para otimizar custos.

### Exemplo em Python:
Abaixo, uma função simples em Python que responde a uma requisição HTTP:

### API Monitoring no Google Cloud Platform (GCP)

O **API Monitoring** no GCP permite acompanhar o desempenho, disponibilidade e integridade das APIs. Utilizando o **API Gateway** e o **Cloud Monitoring**, é possível monitorar métricas-chave, detectar erros e definir alertas para garantir que as APIs estejam funcionando conforme o esperado.

#### Recursos Principais:
- **Métricas e Logs**: Cloud Monitoring oferece métricas de latência, taxa de erros e uso de recursos.
- **Alertas Personalizáveis**: É possível configurar alertas para situações como alta latência ou taxas de erro elevadas, recebendo notificações por e-mail ou outras integrações.
- **Visualização**: Painéis no Console do GCP facilitam a análise em tempo real e o histórico de desempenho da API.

#### Exemplo de Configuração de Alerta para APIs:
1. Acesse **Monitoring > Alerting** no Console do GCP.
2. Crie uma nova política de alerta e escolha as métricas da API (ex.: taxa de erros).
3. Configure as notificações e salve.

API Monitoring é essencial para manter a confiabilidade e performance das APIs em produção.
