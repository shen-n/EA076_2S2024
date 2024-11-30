# `ObservaCÃO - um ajudante para observação do céu noturno`

Este trabalho trata-se do projeto final da disciplina *EA076 (Laboratório de Sistemas Embarcados)*, ministrada pelo Prof. Dr. Fabiano Fruett no segundo semestre de 2024. Ele foi baseado no trabalho "[_Star Track - Arduino Powered Star Pointer and Tracker_](https://www.instructables.com/Star-Track-Arduino-Powered-Star-Pointer-and-Tracke/)", de Görkem, sendo adaptado para operar com a placa BitDogLab.

|Nome do aluno  | RA | Curso|
|--|--|--|
| Felipe Hiroshi Kano Inazumi | 215696  | Eng. Elétrica|
| Nathan Shen Baldon  | 242448 | Eng. Elétrica|

**Table of Contents**

## Descrição do Projeto

O projeto buscou a construção de um sistema capaz de apontar para corpos celestes com um laser, independente da posição do observador. Para isso, deve-se fornecer ao dispositivo as coordenadas do corpo celeste que se deseja observar. Um dos requisitos é que o dispositivo construído fosse _wireless_, ou seja, sem necessidade de cabos para alimentação e comunicação, para que pudesse ser usado em campo com maior facilidade. 

Potenciais usuários:
- amantes de astronomia e astrofotografia;
- educadores;

## Metodologia

### Sistemas de coordenadas

As coordenadas fornecidas ao dispositivo eram conforme o Sistema Horizontal, ou seja, são indicados os valores de Azimute e Altitude de cada corpo celeste. Mais detalhes sobre sistemas de coordenadas são fornecidos no **Apêndice A**, que será utilizado como base para a seção de discussão posteriormente.

|Materiais (colocar link no nome de cada um) | Qtde. | Descrição |
|--|--|--|
|  |   | |
|  |  | |

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








