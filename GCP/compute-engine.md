## Introdução ao Google Compute Engine

O **Google Compute Engine (GCE)** é um serviço de máquinas virtuais (VMs) oferecido pelo Google Cloud Platform que permite criar, gerenciar e executar máquinas virtuais na infraestrutura global do Google. Ele é projetado para suportar aplicações de diversos tamanhos e necessidades, oferecendo flexibilidade e escalabilidade para atender desde pequenos projetos até aplicações de nível corporativo.

## Segurança: Dê a Cesar o que é de Cesar
Foca nas **boas práticas de segurança** ao configurar e gerenciar instâncias de VM. Inclui:
   - **Controle de Acesso**: Uso de Identity and Access Management (IAM) para definir permissões precisas e evitar acessos não autorizados.
   - **Chaves e Autenticação**: Como gerenciar chaves SSH para conexões seguras às VMs.
   - **Firewalls**: Configuração de regras para proteger as VMs contra acessos indesejados, garantindo que apenas portas e endereços IP específicos tenham permissão de entrada.

## VM Instances
Explica o processo de **criação e configuração de instâncias de VM** no GCE:
   - **Escolha de Máquinas Virtuais**: Explicação das diferentes famílias e tipos de VM (ex.: general-purpose, memory-optimized).
   - **Sistema Operacional**: Como selecionar e configurar o sistema operacional, como Linux ou Windows.
   - **Configurações de Rede**: Como conectar a VM a uma rede VPC e configurar IPs públicos e privados.
   - **Customização e Inicialização**: Como usar scripts de inicialização para customizar a VM logo na criação.

## Use VM Groups Para Escalar e Aumentar a Disponibilidade
Introduz **Grupos de Máquinas Virtuais** (VM Groups), que permitem o escalonamento automático e redundância:
   - **Managed Instance Groups (MIGs)**: Configuração de grupos gerenciados que escalam automaticamente com base em métricas, como CPU ou uso de rede.
   - **Desempenho e Redundância**: Garantem alta disponibilidade e balanceamento de carga para aplicações distribuídas.
   - **Rolling Updates**: Como realizar atualizações de software e sistema sem interromper o funcionamento da aplicação.

## AutoScaling e AutoHealing
Explora as funcionalidades de **AutoScaling** e **AutoHealing**:
   - **AutoScaling**: Permite que as VMs escalem automaticamente conforme a demanda aumenta, economizando custos quando a demanda diminui.
   - **AutoHealing**: Monitora a saúde das instâncias e substitui automaticamente VMs com problemas, garantindo que o sistema continue operando sem falhas.

## Quotas e Limites para GCE
Aborda as **quotas e limites** para evitar interrupções no uso dos recursos:
   - **Quotas**: São limites predefinidos para controlar o uso de recursos (ex.: número de CPUs, quantidade de armazenamento).
   - **Monitoramento**: Como monitorar e entender os limites para evitar problemas de escalabilidade.
   - **Solicitação de Aumento**: Explicação sobre como solicitar aumento de quotas, caso o projeto necessite de mais recursos.

## Mas e se eu Precisar de um Servidor Dedicado?
Apresenta a opção de **servidores dedicados**, ideais para workloads que precisam de **isolamento total**:
   - **Servidores Dedicados vs. Compartilhados**: Vantagens do isolamento para cargas de trabalho críticas ou reguladas.
   - **Máquinas Bare Metal**: Como o Google oferece opções de servidores físicos sem virtualização, para casos de uso especializados.

## Gerenciamento de Discos no Google Cloud
Foca no **gerenciamento de discos** para VMs:
   - **Tipos de Discos**: Explica as opções de discos, incluindo Persistent Disks (Standard e SSD) e Local SSDs, e quando usar cada um.
   - **Expansão de Capacidade**: Como expandir o armazenamento de uma VM sem downtime.
   - **Snapshots e Backups**: Configuração de snapshots para criar backups dos discos, facilitando a restauração.

## Snapshots - O que são e para que servem?
Apresenta o conceito de **Snapshots**, que são imagens dos discos de VM:
   - **Criar Snapshots**: Como configurar e automatizar snapshots para backups regulares.
   - **Recuperação Rápida**: Snapshots permitem recuperação rápida em caso de falhas ou perda de dados.
   - **Custos e Otimização**: Boas práticas para gerenciar snapshots e minimizar os custos de armazenamento.

## Economize tempo de Deploy e Configuração com Imagens Públicas e Custom Images
Explora como **imagens públicas e customizadas** podem acelerar o deployment:
   - **Imagens Públicas**: Google oferece imagens prontas para uso com sistemas operacionais comuns e software básico.
   - **Imagens Customizadas**: Criar imagens personalizadas para replicar configurações específicas em novas VMs, economizando tempo de configuração.
   - **Gerenciamento de Imagens**: Como armazenar e versionar imagens para garantir consistência em novos deployments.

## Criando uma Regra de Firewall Simples para PostgreSQL
Demonstra como **configurar regras de firewall** para permitir o acesso seguro ao banco de dados PostgreSQL:
   - **Configuração de Porta e IP**: Como abrir a porta do PostgreSQL (5432) apenas para endereços IP específicos.
   - **Segurança de Rede**: Importância de limitar o acesso a fontes confiáveis para proteger o banco de dados.
   - **Testes e Validação**: Como testar a conectividade para garantir que a regra de firewall esteja funcionando conforme esperado.
