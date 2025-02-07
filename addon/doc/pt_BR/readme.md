# NVDAUpdate Channel Selector #

* Autor: Jose Manuel Delicado
* Compatibilidade com NVDA: 2023.3.4 e posterior
* Download [versão estável][1]

Esse complemento permite fazer download e instalar a versão mais recente do
NVDA do tipo escolhido sem visitar nenhuma página da Web nem usar o
navegador da Web. Ele é útil quando, por exemplo, você deseja testar novos
recursos em um instantâneo do NVDA e depois retornar à versão estável mais
recente. Se você testa regularmente os instantâneos do NVDA e costuma
instalá-los em seu computador, economizará muito tempo com esse
complemento. Se preferir testar instantâneos no modo portátil, mantendo
inalterada a cópia instalada do NVDA, esse complemento também é para você.

## Uso

Você pode alterar o canal de atualização do NVDA acessando o menu NVDA,
Preferências, Configurações, categoria Canal de atualização. Depois de
escolher o canal desejado e pressionar OK, aguarde até a próxima verificação
de atualização automática ou acesse o menu de ajuda do NVDA e escolha a
opção “Verificar atualizações". Por enquanto, estes são os canais
disponíveis:

* Padrão: esse é o canal padrão usado por sua versão do NVDA. Escolher essa
  opção significa o mesmo que desativar o complemento.
* Estável: força o canal de atualização para estável. Útil quando você
  deseja retornar a uma versão estável a partir de um instantâneo.
* Rc e beta: este é o canal para versões beta. Você receberá a primeira
  versão beta assim que ela for lançada. Esse canal permite que você
  atualize por meio de versões beta e candidatas a lançamento.
* Alpha (instantâneos): escolha essa opção para atualizar para a versão alfa
  mais recente. Os instantâneos alfa permitem que você teste novos recursos,
  mas são bastante instáveis. Por favor, tenha cuidado.
* Desabilitar atualizações (não recomendado): essa opção desativa o canal de
  atualização. Se você verificar se há atualizações, será exibida uma
  mensagem de erro. Lembre-se de que pode desativar as atualizações
  automáticas na categoria Configurações gerais. Use essa opção somente para
  fins de teste.

As informações sobre as atualizações disponíveis para cada canal serão
recuperadas em segundo plano quando o painel de configurações for
aberto. Pressione tab para navegar até um campo de edição somente leitura,
onde você pode ver essas informações. Essas informações serão atualizadas
dinamicamente quando você alterar o canal de atualização na caixa de
combinação. Se houver uma atualização disponível para o canal selecionado,
um ou dois links serão exibidos ao lado do campo de edição:

* Download: pressione a barra de espaço neste link para abri-lo em seu
  navegador da Web e fazer o download do instalador mais recente.
* Exibir registro de alterações: pressione a barra de espaço neste link para
  abrir o documento Novidades em seu navegador da Web. Em alguns canais,
  esse link não será exibido.

## Registro de alterações

### Versão 1.4

* Traduções atualizadas.
* Compatível com o NVDA 2023.1.
* Por motivos de segurança, a versão mínima do NVDA está definida como
  2022.4.

### Versão 1.3

* Traduções atualizadas.
* Corrigido um bug que impedia a criação de cópias portáteis a partir de
  instantâneos alfa.

### Versão 1.2

* Traduções atualizadas.
* Compatível com o NVDA 2022.1.
* Por motivos de segurança, a versão mínima do NVDA está definida como
  2021.3.
* Solução alternativa para um bug no servidor NV Access que fazia com que a
  versão 2019.2.1 fosse oferecida ao atualizar de alfa para estável.

### Versão 1.1

* Remoção de canais sem suporte.
* Traduções atualizadas.
* Adicionadas informações sobre as atualizações disponíveis no momento ao
  painel de configurações.

### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=updateChannel
