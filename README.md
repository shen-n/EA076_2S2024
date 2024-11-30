# `ObservaCÃO - um ajudante para observação do céu noturno`

Este trabalho trata-se do projeto final da disciplina *EA076 (Laboratório de Sistemas Embarcados)*, ministrada pelo Prof. Dr. Fabiano Fruett no segundo semestre de 2024. Ele foi baseado no trabalho "[_Star Track - Arduino Powered Star Pointer and Tracker_](https://www.instructables.com/Star-Track-Arduino-Powered-Star-Pointer-and-Tracke/)", de Görkem, sendo adaptado para operar com a placa BitDogLab.

|Nome do aluno  | RA | Curso|
|--|--|--|
| Felipe Hiroshi Kano Inazumi | 215696  | Eng. Elétrica|
| Nathan Shen Baldon  | 242448 | Eng. Elétrica|

Foi também desenvolvido um **MANUAL DE USO**, que pode ser encontrado [aqui](https://github.com/shen-n/EA076_2S2024/blob/main/manual_de_uso.md). 

## Descrição do Projeto

O projeto buscou a construção de um sistema capaz de apontar para corpos celestes com um laser, independente da posição do observador. Para isso, deve-se fornecer ao dispositivo as coordenadas do corpo celeste que se deseja observar. Um dos requisitos é que o dispositivo construído fosse _wireless_, ou seja, sem necessidade de cabos para alimentação e comunicação, para que pudesse ser usado em campo com maior facilidade. 

Potenciais usuários:
- amantes de astronomia e astrofotografia;
- educadores;

## Metodologia

O desenvolvimento deste projeto envolveu quatro frentes: (a) estudo teórico sobre localização de corpos celestes (resumido no sistemas de coordenadas escolhido); (b) escolha de materiais; (c) desenvolvimento e fabricação de uma estrutura mecânica; (d) desenvolvimento e fabricação de uma PCB; (e) desenvolvimento do programa. 

### Sistemas de coordenadas

As coordenadas fornecidas ao dispositivo eram conforme o Sistema Horizontal, ou seja, são indicados os valores de Azimute e Altitude de cada corpo celeste. Mais detalhes sobre sistemas de coordenadas são fornecidos no **Apêndice A**, que será utilizado como base para a seção de discussão posteriormente.

### Materiais Utilizados

Os materiais escolhidos e utilizados são descritos na tabela a seguir. Se desejado, pode-se clicar no nome do material para ser redirecionado para o site de um fornecedor.

|Materiais | Qtde. | Descrição |
|--|--|--|
| [Placa BitDogLab](https://github.com/BitDogLab/BitDogLab/tree/main) | 1 | Controle do projeto. Além disso, os botões e joystick da placa também foram utilizados para controle pelo usuário. |
| [Motor de Passo 17HS4023](https://pt.aliexpress.com/item/1005007232266402.html?src=google&src=google&albch=shopping&acnt=768-202-3196&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005007232266402&ds_e_product_merchant_id=107776500&ds_e_product_country=BR&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=21451844582&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjwufq2BhAmEiwAnZqw8ryQpUhfJJZnJBBU1dzkV41koB3Xd2dV5Wr7NiGT26p2H47F2nBP8BoCk3AQAvD_BwE#nav-description) | 2 | Para movimentar o laser. |
| [Driver DRV8825](https://pt.aliexpress.com/item/4000083334758.html?spm=a2g0o.productlist.main.1.1ee63b5dYR0HFh&algo_pvid=f9678024-8e61-435d-b24b-e7b03aa366c1&algo_exp_id=f9678024-8e61-435d-b24b-e7b03aa366c1-0&pdp_npi=4%40dis%21BRL%219.17%219.17%21%21%211.55%211.55%21%402101fb0b17259175411665778e296c%2110000000221353262%21sea%21BR%21820637743%21X&curPageLogUid=1fFYR8MPnuXO&utparam-url=scene%3Asearch%7Cquery_from%3A) | 2 | Para realizar a interface entre BitDogLab e motores. Este driver utiliza a interface STEP/DIR, que facilita o controle dos motores, sendo necessários apenas 2 pinos na BitDogLab. |
| [Bateria 3S](https://pt.aliexpress.com/item/1005003835491136.html?spm=a2g0o.productlist.main.1.35611c4axpUbnB&algo_pvid=e869b7f9-aebd-43ff-8cf8-b699134a31af&algo_exp_id=e869b7f9-aebd-43ff-8cf8-b699134a31af-0&pdp_npi=4%40dis%21BRL%21335.05%21184.30%21%21%2152.54%2128.90%21%402103237317330016817741462e31ea%2112000038628969519%21sea%21BR%21820637743%21X&curPageLogUid=6e8nIrLFmuko&utparam-url=scene%3Asearch%7Cquery_from%3A) | 1 | Para que o ObservaCÃO seja independente da rede elétrica. |
| [Laser](https://pt.aliexpress.com/item/1005006719063413.html?spm=a2g0o.productlist.main.47.5b528DSC8DSCZL&algo_pvid=fd9bea5f-df14-442b-9f88-218b0c320ad9&aem_p4p_detail=202411301313296697071011177370001865716&algo_exp_id=fd9bea5f-df14-442b-9f88-218b0c320ad9-23&pdp_npi=4%40dis%21BRL%2121.87%2120.34%21%21%213.43%213.19%21%402103201917330012093146250ef29e%2112000038085388176%21sea%21BR%21820637743%21X&curPageLogUid=5TyeX89aGz4e&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202411301313296697071011177370001865716_6) | 1 | Para apontar para os corpos celestes. |
| [Módulo Bluetooth HC-05](https://www.eletrogate.com/modulo-bluetooth-rs232-hc-05?utm_source=Site&utm_medium=GoogleMerchant&utm_campaign=GoogleMerchant&utm_source=google&utm_medium=cpc&utm_campaign=[MC4]_[G]_[PMax]_Categorias&utm_content=&utm_term=&gad_source=1&gclid=CjwKCAiAjKu6BhAMEiwAx4UsAqtbrS_S_TdBN0OxV5r_2TgRlhCnLvffXhJ7JxJXbR2puQFTbAGGFxoC9gUQAvD_BwE) | 1 | Para que as coordenadas dos corpos celestes fossem passadas para a BitDogLab sem necessidade de fios. |
| [Parafusos M3 10 mm](https://pt.aliexpress.com/item/1005007219475077.html?spm=a2g0o.productlist.main.21.6a963d1dzLJ7hc&algo_pvid=9d594b07-ea1f-4dd6-a3d9-85259d659b2e&algo_exp_id=9d594b07-ea1f-4dd6-a3d9-85259d659b2e-10&pdp_npi=4%40dis%21BRL%218.16%218.16%21%21%211.28%211.28%21%402103010e17330013153847143ee080%2112000039933522857%21sea%21BR%21820637743%21X&curPageLogUid=s4zueP23lyjy&utparam-url=scene%3Asearch%7Cquery_from%3A) | 4 | Para montagem de um dos motores de passo na estrutura mecânica. |
| [Conector XT30pw fêmea 90 graus](https://pt.aliexpress.com/item/1005004957495676.html?spm=a2g0o.productlist.main.19.3151uBL9uBL9SF&algo_pvid=02c4525d-b678-4c0e-b519-59ae541b0730&algo_exp_id=02c4525d-b678-4c0e-b519-59ae541b0730-9&pdp_npi=4%40dis%21BRL%211.66%211.66%21%21%210.26%210.26%21%402103247917330014227191664ed1a2%2112000031154779399%21sea%21BR%21820637743%21X&curPageLogUid=xKBgxkLjv4B9&utparam-url=scene%3Asearch%7Cquery_from%3A) | 1 | Para conexão da bateria na PCB criada. |
| [Cabo com conector JST 4 pinos](https://www.makerhero.com/produto/conector-jst-4-pinos-femea/?gad_source=1&gclid=CjwKCAiAjKu6BhAMEiwAx4UsAl4_gJ-5PNdV9rmTd0kF7blvSqFHF_JUx8ye31I1oftJEZEbPSfr_xoC_MgQAvD_BwE) | 4 | Para conexão entre a BitDogLab e a PCB desenvolvida. |
| [Conector JST 4 pinos macho (I2C)](https://www.makerhero.com/produto/conector-jst-4-pinos-macho/) | 3 | Utilizados na PCB criada para conexão com a BitDogLab. |
| [Conector IDC Box 14 pinos macho](https://pt.aliexpress.com/item/1005006804603387.html?spm=a2g0o.productlist.main.13.2c401d35aEuDLu&algo_pvid=dce204da-6e38-47c0-a5cd-3767e274d56a&algo_exp_id=dce204da-6e38-47c0-a5cd-3767e274d56a-6&pdp_npi=4%40dis%21BRL%2124.45%217.83%21%21%2127.78%218.89%21%402101ef7017330015717997979e2204%2112000038361940664%21sea%21BR%21820637743%21X&curPageLogUid=l8cuuroPD1VO&utparam-url=scene%3Asearch%7Cquery_from%3A) | 1 | Utilizado na PCB criada para conexão com a BitDogLab. |
| [Cabo flat com conector IDC Box 14 pinos](https://pt.aliexpress.com/item/1005003161799870.html?spm=a2g0o.productlist.main.5.794a6cb4IXeVPj&algo_pvid=c761506e-c609-41e1-ae3f-59f78ccbfad8&algo_exp_id=c761506e-c609-41e1-ae3f-59f78ccbfad8-2&pdp_npi=4%40dis%21BRL%2128.06%218.16%21%21%214.40%211.28%21%402103237317330016535638644e31ea%2112000024427578485%21sea%21BR%21820637743%21X&curPageLogUid=HS1RQDKcrUE4&utparam-url=scene%3Asearch%7Cquery_from%3A) | 1 | Para conexão entre a BitDogLab e a PCB desenvolvida. |

### Estrutura Mecânica


### Fluxograma

## Descrição Estrutural



### Conexões com BitDogLab
<table><thead><tr><th></th><th>Pino</th><th>GPIO</th><th>Conector BitDogLab</th></tr></thead><tbody><tr><td rowspan="5">Driver 1 (motor Altitude)</td><td>M0</td><td>19</td><td rowspan="10">IDC box 14 pinos</td></tr><tr><td>M1</td><td>20</td></tr><tr><td>M2</td><td>18</td></tr><tr><td>DIR</td><td>4</td></tr><tr><td>STEP</td><td>28</td></tr><tr><td rowspan="5">Driver 2 (motor Azimute)</td><td>M0</td><td>19</td></tr><tr><td>M1</td><td>20</td></tr><tr><td>M2</td><td>18</td></tr><tr><td>DIR</td><td>17</td></tr><tr><td>STEP</td><td>16</td></tr><tr><td>Laser</td><td>-</td><td>2 (SDL)</td><td>I2C1</td></tr><tr><td rowspan="4">Módulo Bluetooth HC-05</td><td>RX</td><td>0 (SDA)</td><td rowspan="4">I2C0</td></tr><tr><td>TX</td><td>1 (SCL)</td></tr><tr><td>VCC</td><td>3V3</td></tr><tr><td>GND</td><td>GND</td></tr></tbody></table>

![Alt text](images/diagrama.png)


## Resultados

## Desafios e Conclusão

## Referências

## Apêndice A - sistemas de coordenadas

Para localizar os corpos celestes, é muito comum que se utilize o sistema de coordenadas celeste. Nele, usa-se o conceito de Esfera Celeste: uma projeção de todo o céu em uma esfera de raio indeterminado e concêntrica à Terra (como se o céu que vemos fosse uma casca esférica ao redor da Terra). A localização dos corpos se dá através de coordenadas esféricas, às quais dependem do plano fundamental escolhido (plano que divide Esfera Celeste em dois hemisférios) [1]. O Sistema Horizontal, por exemplo, é geralmente mais conhecido (com Azimute/Altitude como coordenadas) e utiliza o horizonte local do observador como plano fundamental [1,7]. O problema é que, como a referência (plano fundamental) depende da posição do observador na Terra, a posição do corpo celeste a ser apontado, por consequência, também depende. Assim, para eliminar essa dependência, é comum que se utilize o Sistema Equatorial, que toma como plano fundamental o Equador Celeste (projeção da Linha do Equador na Esfera Celeste) [1,6]. O Polo Norte e Polo Sul também são projetados na Esfera Celeste, sendo denominados Polo Sul Celeste e Polo Norte Celeste (Fig.1).

As coordenadas são dadas em Ascenção Reta e Declinação:
- Declinação (DEC): ângulo entre Equador Celeste e Polos Norte ou Sul Celestes (varia de -90 a 90°).
- Ascensão Reta (RA): ângulo ao longo do Equador Celeste em relação a uma referência zero (ponto vernal - equivalente ao Meridiano de Greenwich como referência de longitude). Ele é dado em horas, minutos e segundos, de forma que uma volta completa equivale a 24h.

Assim, para localizar os corpos celestes, será utilizada uma base de dados que indique as coordenadas no Sistema Equatorial [1,8]. Também, o sistema deverá saber onde estão as referências de posição necessárias:
- Referência para DEC: uma alternativa é encontrar o Polo Norte Celeste, que pode ser encontrado através da Estrela Polar (Polaris) [1,4,5]. Assim, seria necessário apontar para esta Estrela manualmente, indicando para o sistema sua posição.
- Referência para RA: será utilizado o tempo sideral, que também tem como referência o ponto vernal (referência de RA). O tempo sideral pode ser calculado com o horário local. [1]








