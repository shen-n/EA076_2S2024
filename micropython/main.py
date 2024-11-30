# Libraries
from machine import Pin
from time import sleep_ms, sleep
import sys
from machine import Pin, ADC, SoftI2C, PWM
from ssd1306 import SSD1306_I2C
import framebuf
import neopixel
import time
import random
from machine import Pin, UART


############## INIT/CONFIG PORTS
        
 # Configura UART0
uart = UART(0, 9600)

# Inicializa o joystick
adc_x = ADC(Pin(27))
adc_y = ADC(Pin(26))
joystick_button = Pin(22, Pin.IN, Pin.PULL_UP)

# Define os valores mínimos e máximos dos conversores AD
adc_min = 300
adc_max = 65535
adc_avg = int((adc_max-adc_min)/2)
tol = 30000 # tolerance to arbitrate between right/left movement

# Inicialização de variáveis para controle do display OLED.
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)

# Configura pinos de microstep do motor
m0Pin = Pin(19, Pin.OUT)
m1Pin = Pin(20, Pin.OUT)
m2Pin = Pin(18, Pin.OUT)

# create an output pin on pin #0
dirPin_zen = Pin(4, Pin.OUT) #laser
stepPin_zen = Pin(28, Pin.OUT) #laser
dirPin_azi = Pin(17, Pin.OUT) #base
stepPin_azi = Pin(16, Pin.OUT) #base

laserPin = Pin(2, Pin.OUT) # laser

laserPin.value(1)

botao_b = Pin(6, Pin.IN, Pin.PULL_UP)
button_a = Pin(5, Pin.IN, Pin.PULL_UP)


############## FUNCTIONS

# takes a step (Azimuth)
def step_x():
    stepPin_azi.value(1)
    sleep_ms(3)
    stepPin_azi.value(0)
    sleep_ms(3)
    
# takes a step (Zenith)
def step_y():
    stepPin_zen.value(1)
    sleep_ms(3)
    stepPin_zen.value(0)
    sleep_ms(3)

# indicates if joystick is being pushed up or down
def up_or_down(adc_value, adc_avg):
    if (adc_value<(adc_avg-tol)):
        return 'up'
    if adc_value>(adc_avg+tol):
        return 'down'
    else:
        return None

# indicates if joystick is being pushed to the left or to the right
def left_or_right(adc_value, adc_avg):
    if (adc_value<(adc_avg-tol)):
        return 'left'
    if adc_value>(adc_avg+tol):
        return 'right'
    else:
        return None
    
# converts angle (degrees) to step (1/32 microstepping)
# 1 step = 1.8 degrees
def degrees2step(angle):
    microstep = 1.8/32 # degrees
    n_steps = int(angle/microstep)
    return n_steps

# sets new reference for Zenith and Azimuth angles
def set_reference():
    azi_angle = 0
    zen_angle = 0

def recalibrate(dirPin_x, dirPin_y, adc_x, adc_y, joystick_button, botao_b, oled):
    previous_pos_x = None
    previous_pos_y = None
    joystick_button_pressed = False
    micro_adjust = False
    
    oled.fill(0)
    oled.text("CALIBRACAO", 20, 15)
    oled.show()
    
    button_b_pressed = False

    while True:
        adc_value_x = adc_x.read_u16()
        adc_value_y = adc_y.read_u16()
   
        current_pos_x = left_or_right(adc_value_x, adc_avg)
        current_pos_y = up_or_down(adc_value_y, adc_avg)
        
        
        joystick_button_state = joystick_button.value()
        
        if joystick_button_state == 0 and not joystick_button_pressed:
            joystick_button_pressed = True
            micro_adjust = not micro_adjust
        
    
        if joystick_button_state == 1:
            joystick_button_pressed = False
        
        
        if current_pos_x == 'right':                  
            if previous_pos_x != 'right':
                oled.text("DIREITA", 30, 50)
                oled.show()
                dirPin_x.value(0)
                previous_pos_x = 'right'

            
            step_x()
            if micro_adjust:
                sleep_ms(50)
                
        elif current_pos_x == 'left':            
            if previous_pos_x != 'left':
                oled.text("ESQUERDA", 30, 50)
                oled.show()
                dirPin_x.value(0)
                dirPin_x.value(1)
                previous_pos_x = 'left'

            
            step_x()
            if micro_adjust:
                sleep_ms(50)
        
        elif current_pos_x == None:
            if previous_pos_x != None:
                previous_pos_x = None
                oled.fill(0)
                oled.text("CALIBRACAO", 20, 15)
                oled.show()

        
        
        if current_pos_y == 'up':                  
            if previous_pos_y != 'up':
                oled.text("CIMA", 30, 50)
                oled.show()
                dirPin_y.value(0)
                previous_pos_y = 'up'

            
            
            if micro_adjust:
                sleep_ms(50)
            step_y()
                
        elif current_pos_y == 'down':            
            if previous_pos_y != 'down':
                oled.text("BAIXO", 30, 50)
                oled.show()
                dirPin_y.value(1)
                previous_pos_y = 'down'

            
            
            if micro_adjust:
                sleep_ms(50)
            step_y()
        
        elif current_pos_y == None:
            if previous_pos_y != None:
                oled.fill(0)
                oled.text("CALIBRACAO", 20, 15)
                oled.show()
                previous_pos_y = None
        
        if botao_b.value()==0:
            button_b_pressed = True
        
        elif button_b_pressed and botao_b.value():
            return 0,0
 
            


############## MAIN

# configures microstep pins (to 1/32)
m0Pin.value(1)
m1Pin.value(1)
m2Pin.value(1)

# sets initial reference (for Zenith and Azimuth angles):
zen_angle = 0
azi_angle = 0


zen_angle, azi_angle = recalibrate(dirPin_azi, dirPin_zen, adc_x, adc_y, joystick_button, botao_b, oled)

oled.fill(0)
oled.text("ENVIE COORDENADAS", 0,15)
oled.text("NO FORMATO", 25,25)
oled.text("Azimuth,Altitude", 0,45)
oled.show()

led_state = 0
laserPin.value(1)

while True:
    
    ############## Zenith
    
    uart.write('Zenith Angle (0 a 90): \n')
    
    # flags
    wait = True
    button_b_pressed = False
    button_a_pressed = False
    
    while wait:
        if botao_b.value() == 0:
            button_b_pressed = True
        elif botao_b.value() == 1 and button_b_pressed:
            button_b_pressed = False
            zen_angle, azi_angle = recalibrate(dirPin_azi, dirPin_zen, adc_x, adc_y, joystick_button, botao_b, oled)
            oled.fill(0)
            oled.text("ENVIE COORDENADAS", 0,15)
            oled.text("NO FORMATO", 25,25)
            oled.text("Azimuth,Altitude", 0,45)
            oled.show()
        
        if button_a.value() == 0:
            button_a_pressed = True
        elif button_a.value() == 1 and button_a_pressed:
            # Led Desligado
            if led_state == 0:
                led_state = 2
                laserPin.value(0)
            
            # Led Liga no final do movimento
            elif led_state == 1:
                led_state = 2
                #laserPin.value(0)
            
            # Led sempre ligado
            elif led_state == 2:
                led_state = 0
                laserPin.value(1)
            button_a_pressed = False
           
        if uart.any():  # Verifica se há dados disponíveis
            data = uart.read().decode('utf-8').strip()  # Lê os dados, decodifica e remove espaços em branco
            try:
                # Divide os dados recebidos na vírgula
                values = data.split(',')
                if len(values) == 2:  # Certifica-se de que há exatamente dois valores
                    azi_input = float(values[0])  # Converte o primeiro valor para inteiro
                    zen_input = float(values[1])  # Converte o segundo valor para inteiro
                    wait = False
                    print(f"Zenith: {zen_input}, Azimuth: {azi_input}")
            except ValueError:
                print("Dados recebidos inválidos. Certifique-se de enviar no formato 20,20.")
    
    if azi_input > 180:
        azi_input = (-1)*(360 - azi_input)

    if led_state == 1:
        laserPin.value(0)
                        
    # calculates the needed rotation to reach the input angle
    zen = zen_input - zen_angle
    
    # determines direction of rotation 
    if zen<0:
        dirPin_zen.value(1)
        zen = -zen # turns into positive number
    else:
        dirPin_zen.value(0)
        
    # converts calculated angle in degrees to number of microsteps (1/32) needed
    zen_steps = degrees2step(zen)
    
    ############## Azimuth
        

    uart.write('Zenith Angle: {} deg. \n'.format(zen_input))
    uart.write('Azimuth Angle: {} deg. \n'.format(azi_input))

    # calculates the needed rotation to reach the input angle
    azi = azi_input-azi_angle
    
    # determines direction of rotation 
    if azi<0:
        dirPin_azi.value(1)
        azi = -azi # turns into positive number
    else:
        dirPin_azi.value(0)
    
    # converts calculated angle in degrees to number of microsteps (1/32) needed
    azi_steps = degrees2step(azi)
    
    # displays configured angles in the OLED
    oled.fill(0)

    oled.text("-"*30,0,0)
    oled.text(f"AZIMUTH: {azi_input:.2f}", 5, 10)
    oled.text(f"ALTITUDE: {zen_input:.2f}", 5, 25)

    oled.text("-"*30,0,35)
        
        
    oled.text("A: LASER", 5, 45)
    oled.text("B: CALIBRACAO", 5, 55)

    oled.show()
    
    # moves to new position
    for i in range(azi_steps):
        step_x()
    for i in range (zen_steps):
        step_y()
        
    # update current position (in relation to the reference set earlier)
    zen_angle = zen_input
    azi_angle = azi_input
    
    if led_state == 1:
        laserPin.value(1)
