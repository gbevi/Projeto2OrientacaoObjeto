from matplotlib import pyplot as plt
import os
from matplotlib.patches import *
from package.maths.terms import *
from package.maths.model import *
import numpy as np

def handle_ponto():   
    try:
        user_input = float(input('Digite a coordenada x: '))
    except ValueError:
        print('Erro: Por favor, digite um número válido para a coordenada x.')
    try:
        user_input_2 = float(input('Digite a coordenada y: '))
    except ValueError:
        print('Erro: Por favor, digite um número válido para a coordenada y.')
    os.system('cls' if os.name == 'nt' else 'clear')
    ponto_1 = ponto(user_input, user_input_2)
    Cena.add_forma(ponto_1)
    print(f"A distância do ponto para a origem é: {ponto_1.distanciaDe0()}")
    ponto_1.model()
    print(f'\033[31mPor favor, quando estiver pronto(a), clique no "x" do gráfico para continuar\033[0m')
    plt.plot(user_input, user_input_2, 'ro')
    plt.show()

def handle_reta():
    user_input = float(input('Digite a coordenada x: '))
    user_input_2 = float(input('Digite a coordenada y: '))
    user_input_3 = float(input('Digite o valor de a: '))
    user_input_4 = float(input('Digite o valor de b: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    segmento_1 = Reta(user_input_3, user_input_4, user_input, user_input_2)
    Cena.add_forma(segmento_1)
    segmento_1.coordenadas()
    print(f'Interpolando, y = {segmento_1.interpolar():.2f}')
    print(f'\033[31mPor favor, quando estiver pronto(a), clique no "x" do gráfico para continuar\033[0m')
    plt.plot([0, segmento_1.getX()[0]], [segmento_1.getB(), segmento_1.interpolar()])
    plt.show()

def handle_circulo():
    user_input = float(input('Digite a coordenada x: '))
    user_input_2 = float(input('Digite a coordenada y: '))
    user_input_3 = float(input('Digite o valor do raio: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    circulo_1 = Circulo(user_input, user_input_2, user_input_3)
    Cena.add_forma(circulo_1)
    circulo_1.model()
    circulo_1.distancia()
    print(f'A área do circulo é: {circulo_1.area():.2f}')
    print(f'O perímetro do circulo é: {circulo_1.perimetro():.2f}')
    print(f'\033[31mPor favor, quando estiver pronto(a), clique no "x" do gráfico para continuar\033[0m')

    fig, ax = plt.subplots()
    circle = Circle((circulo_1.getX(),circulo_1.getY()),circulo_1.getRaio(),fill=False)
    ax.add_patch(circle)
    ax.set_xlim(circulo_1.getX()[0] - circulo_1.getRaio() - 1, circulo_1.getX()[0] + circulo_1.getRaio() + 1)
    ax.set_ylim(circulo_1.getY()[0] - circulo_1.getRaio() - 1, circulo_1.getY()[0] + circulo_1.getRaio() + 1)
    ax.set_aspect('equal')
    plt.show()

def handle_triangulo():
    user_input = float(input('Digite a coordenada x1: '))
    user_input_2 = float(input('Digite a coordenada y1: '))
    user_input_3 = float(input('Digite a coordenada x2: '))
    user_input_4 = float(input('Digite a coordenada y2: '))
    user_input_5 = float(input('Digite a coordenada x3: '))
    user_input_6 = float(input('Digite a coordenada y3: '))
    os.system('cls' if os.name == 'nt' else 'clear')
            
    x = [user_input, user_input_3, user_input_5]
    maxX = max(x)
    minX = min(x)
    y = [user_input_2, user_input_4, user_input_6]
    maxY = max(y)
    minY = min(y)
    trianguloCheck = triangulo(x,y)
    Cena.add_forma(trianguloCheck)
    trianguloCheck.area()
    if trianguloCheck.isValidTriangle() == False:
        print('Triangulo inválido')
    else:
        trianguloCheck.model()
        trianguloCheck.TipoTriangulo()
        print(f'O perímetro do triangulo é: {trianguloCheck.perimetro():.2f}')
        print(f'A área do triangulo é: {trianguloCheck.area():.2f}')
        print(f'\033[31mPor favor, quando estiver pronto(a), clique no "x" do gráfico para continuar\033[0m')
        plt.plot([user_input,user_input_3,user_input_5,user_input],[user_input_2,user_input_4,user_input_6,user_input_2])
        ax = plt.gca()
        ax.set_xlim(minX - 1, maxX + 1)
        ax.set_ylim(minY - 1, maxY + 1)
        ax.set_aspect('equal')
        plt.show()

def handle_quadrado():
    user_input = float(input('Digite a coordenada x1: '))
    user_input_2 = float(input('Digite a coordenada y1: '))
    user_input_3 = float(input('Digite a coordenada x2: '))
    user_input_4 = float(input('Digite a coordenada y2: '))
    os.system('cls' if os.name == 'nt' else 'clear')

    x = [user_input, user_input_3]
    y = [user_input_2, user_input_4]
    quadrado_1 = quadrado(x, y)
    if quadrado_1.isValidSquare() == False:
        print('Quadrado inválido')
    else:
        Cena.add_forma(quadrado_1)
        quadrado_1.model()
        print(f'O perímetro do quadrado é: {quadrado_1.perimetro():.2f}')
        print(f'A área do quadrado é: {quadrado_1.area():.2f}')

        # Step 1: Determine the center point
        center_x = (user_input + user_input_3) / 2
        center_y = (user_input_2 + user_input_4) / 2

        # Step 2 & 3: Calculate the diagonal and side length
        diagonal = np.sqrt((user_input_3 - user_input)**2 + (user_input_4 - user_input_2)**2)
        side = diagonal / np.sqrt(2)

        # Step 4: Calculate the angle of rotation
        angle = np.arctan2(user_input_4 - user_input_2, user_input_3 - user_input)

        # Step 5: Calculate the four corners of the square
        corners = []
        for i in range(4):
            dx = np.cos(angle + np.pi/2 * i) * side / np.sqrt(2)
            dy = np.sin(angle + np.pi/2 * i) * side / np.sqrt(2)
            corners.append((center_x + dx, center_y + dy))

        # Convert corners to a format suitable for plt.plot
        x_corners, y_corners = zip(*corners)
        x_corners += (x_corners[0],)  # Close the square by repeating the first point at the end
        y_corners += (y_corners[0],)

        # Step 6: Plot the square
        plt.figure()
        plt.plot(x_corners, y_corners, '-o')  # '-o' to mark corners
        plt.xlim(min(x_corners) - 1, max(x_corners) + 1)
        plt.ylim(min(y_corners) - 1, max(y_corners) + 1)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

def handle_retangulo():
    user_input = float(input('Digite a coordenada x1: '))
    user_input_2 = float(input('Digite a coordenada y1: '))
    user_input_3 = float(input('Digite a coordenada x2: '))
    user_input_4 = float(input('Digite a coordenada y2: '))
    user_input_5 = float(input('Digite a coordenada x3: '))
    user_input_6 = float(input('Digite a coordenada y3: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    x = [user_input, user_input_3, user_input_5]
    y = [user_input_2, user_input_4, user_input_6]
    retangulo_1 = retangulo(x, y)
    if retangulo_1.isValidRectangle() == False:
        print('Retangulo inválido')
    else:
        Cena.add_forma(retangulo_1)
        retangulo_1.model()
        print(f'O perímetro do retangulo é: {retangulo_1.perimetro():.2f}')
        print(f'A área do retangulo é: {retangulo_1.area():.2f}')
        print(f'\033[31mPor favor, quando estiver pronto(a), clique no "x" do gráfico para continuar\033[0m')
        x_d = x[0] + x[2] - x[1]
        y_d = y[0] + y[2] - y[1]
    
    # Add D to the list of coordinates
        x.append(x_d)
        y.append(y_d)
    
    # Close the rectangle by adding the first point at the end
        x.append(x[0])
        y.append(y[0])
    
    # Plot the rectangle
        plt.figure()
        plt.plot(x, y, '-o')  # '-o' to mark the vertices
        plt.fill(x, y) 
        plt.xlim(min(x) - 1, max(x) + 1)
        plt.ylim(min(y) - 1, max(y) + 1)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

def handle_trapezio():
    user_input = float(input('Digite a coordenada x1: '))
    user_input_2 = float(input('Digite a coordenada y1: '))
    user_input_3 = float(input('Digite a coordenada x2: '))
    user_input_4 = float(input('Digite a coordenada y2: '))
    user_input_5 = float(input('Digite a coordenada x3: '))
    user_input_6 = float(input('Digite a coordenada y3: '))
    user_input_7 = float(input('Digite a coordenada x4: '))
    user_input_8 = float(input('Digite a coordenada y4: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    x = [user_input, user_input_3, user_input_5, user_input_7]
    y = [user_input_2, user_input_4, user_input_6, user_input_8]
    trapezio_1 = trapezio(x, y)
    if trapezio_1.isValidTrapezium() == False:
        print('Trapézio inválido')
    else:
        Cena.add_forma(trapezio_1)
        trapezio_1.model()
        print(f'O perímetro do trapezio é: {trapezio_1.perimetro():.2f}')
        print(f'A área do trapezio é: {trapezio_1.area():.2f}')
        print(f'\033[31mPor favor, quando estiver pronto(a), clique no "x" do gráfico para continuar\033[0m')
        plt.plot([user_input,user_input_3,user_input_5,user_input_7,user_input],[user_input_2,user_input_4,user_input_6,user_input_8,user_input_2])
        ax = plt.gca()
        ax.set_xlim(min(x) - 1, max(x) + 1)
        ax.set_ylim(min(y) - 1, max(y) + 1)
        ax.set_aspect('equal')
        plt.show()

def handle_lista():
    lista = Cena.get_forma()
    i = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    for forma in lista:
        print(f"{i}. Nome: {forma.__class__.__name__}")
        print(forma)
        i+=1
    input("Pressione enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_help():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Opções disponíveis:")
    print("ponto, reta, circulo, triangulo, quadrado, retangulo, trapezio")
    input("Pressione enter para continuar...")

    

def handle_sair():
    print("Saindo do programa...")
    exit()