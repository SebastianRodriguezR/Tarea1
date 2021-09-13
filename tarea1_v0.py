# coding=utf-8
"""Drawing a Quad via a EBO"""

import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys

__author__ = "Daniel Calderon"
__license__ = "MIT"


# We will use 32 bits data, so floats and integers have 4 bytes
# 1 byte = 8 bits
SIZE_IN_BYTES = 4


# A class to store the application control
class Controller:
    fillPolygon = True


# we will use the global controller as communication with the callback function
controller = Controller()


def on_key(window, key, scancode, action, mods):

    if action != glfw.PRESS:
        return
    
    global controller

    if key == glfw.KEY_SPACE:
        controller.fillPolygon = not controller.fillPolygon

    elif key == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(window, True)

    else:
        print('Unknown key')

def crear_dama(x,y,r,g,b,radius):
    
    circle = []
    for angle in range(0,360,10):
        circle.extend([x, y, 0.0, r, g, b])
        circle.extend([x+np.cos(np.radians(angle))*radius, 
                       y+np.sin(np.radians(angle))*radius, 
                       0.0, r, g, b])
        circle.extend([x+np.cos(np.radians(angle+10))*radius, 
                       y+np.sin(np.radians(angle+10))*radius, 
                       0.0, r, g, b])
    
    return np.array(circle, dtype = np.float32)
def crear_Tablero(shaderProgram):
    
    # Defining locations and colors for each vertex of the shape
    #####################################
    
    vertexData = np.array([
    #   positions        colors
        -0.9, -0.9, 0.0,  1.0, 0.0, 1.0, #0
         0.9, -0.9, 0.0,  1.0, 0.0, 1.0, #1
         0.9,  0.9, 0.0,  1.0, 0.0, 1.0, #2
        -0.9,  0.9, 0.0,  1.0, 0.0, 1.0, #3
        -0.8, -0.8, 0.0,  1.0, 1.0, 1.0, #4
         0.8, -0.8, 0.0,  1.0, 1.0, 1.0, #5
         0.8,  0.8, 0.0,  1.0, 1.0, 1.0, #6
        -0.8,  0.8, 0.0,  1.0, 1.0, 1.0, #7
        -0.8,  0.8, 0.0,  0.0, 0.0, 0.0, #8
        -0.6,  0.8, 0.0,  0.0, 0.0, 0.0, #9
        -0.4,  0.8, 0.0,  0.0, 0.0, 0.0, #10
        -0.2,  0.8, 0.0,  0.0, 0.0, 0.0, #11
         0.0,  0.8, 0.0,  0.0, 0.0, 0.0, #12
         0.2,  0.8, 0.0,  0.0, 0.0, 0.0, #13
         0.4,  0.8, 0.0,  0.0, 0.0, 0.0, #14
         0.6,  0.8, 0.0,  0.0, 0.0, 0.0, #15
        -0.8,  0.6, 0.0,  0.0, 0.0, 0.0, #16
        -0.6,  0.6, 0.0,  0.0, 0.0, 0.0, #17
        -0.4,  0.6, 0.0,  0.0, 0.0, 0.0, #18
        -0.2,  0.6, 0.0,  0.0, 0.0, 0.0, #19
         0.0,  0.6, 0.0,  0.0, 0.0, 0.0, #20
         0.2,  0.6, 0.0,  0.0, 0.0, 0.0, #21
         0.4,  0.6, 0.0,  0.0, 0.0, 0.0, #22
         0.6,  0.6, 0.0,  0.0, 0.0, 0.0, #23
         0.8,  0.6, 0.0,  0.0, 0.0, 0.0, #24
        -0.8,  0.4, 0.0,  0.0, 0.0, 0.0, #25
        -0.6,  0.4, 0.0,  0.0, 0.0, 0.0, #26
        -0.4,  0.4, 0.0,  0.0, 0.0, 0.0, #27
        -0.2,  0.4, 0.0,  0.0, 0.0, 0.0, #28
         0.0,  0.4, 0.0,  0.0, 0.0, 0.0, #29
         0.2,  0.4, 0.0,  0.0, 0.0, 0.0, #30
         0.4,  0.4, 0.0,  0.0, 0.0, 0.0, #31
         0.6,  0.4, 0.0,  0.0, 0.0, 0.0, #32
         0.8,  0.4, 0.0,  0.0, 0.0, 0.0, #33
        -0.8,  0.2, 0.0,  0.0, 0.0, 0.0, #34
        -0.6,  0.2, 0.0,  0.0, 0.0, 0.0, #35
        -0.4,  0.2, 0.0,  0.0, 0.0, 0.0, #36
        -0.2,  0.2, 0.0,  0.0, 0.0, 0.0, #37
         0.0,  0.2, 0.0,  0.0, 0.0, 0.0, #38
         0.2,  0.2, 0.0,  0.0, 0.0, 0.0, #39
         0.4,  0.2, 0.0,  0.0, 0.0, 0.0, #40
         0.6,  0.2, 0.0,  0.0, 0.0, 0.0, #41
         0.8,  0.2, 0.0,  0.0, 0.0, 0.0, #42
        -0.8,  0.0, 0.0,  0.0, 0.0, 0.0, #43
        -0.6,  0.0, 0.0,  0.0, 0.0, 0.0, #44
        -0.4,  0.0, 0.0,  0.0, 0.0, 0.0, #45
        -0.2,  0.0, 0.0,  0.0, 0.0, 0.0, #46
         0.0,  0.0, 0.0,  0.0, 0.0, 0.0, #47
         0.2,  0.0, 0.0,  0.0, 0.0, 0.0, #48
         0.4,  0.0, 0.0,  0.0, 0.0, 0.0, #49
         0.6,  0.0, 0.0,  0.0, 0.0, 0.0, #50
         0.8,  0.0, 0.0,  0.0, 0.0, 0.0, #51

        -0.8, -0.2, 0.0,  0.0, 0.0, 0.0, #52
        -0.6, -0.2, 0.0,  0.0, 0.0, 0.0, #53
        -0.4, -0.2, 0.0,  0.0, 0.0, 0.0, #54
        -0.2, -0.2, 0.0,  0.0, 0.0, 0.0, #55
         0.0, -0.2, 0.0,  0.0, 0.0, 0.0, #56
         0.2, -0.2, 0.0,  0.0, 0.0, 0.0, #57
         0.4, -0.2, 0.0,  0.0, 0.0, 0.0, #58
         0.6, -0.2, 0.0,  0.0, 0.0, 0.0, #59
         0.8, -0.2, 0.0,  0.0, 0.0, 0.0, #60
        -0.8, -0.4, 0.0,  0.0, 0.0, 0.0, #61
        -0.6, -0.4, 0.0,  0.0, 0.0, 0.0, #62
        -0.4, -0.4, 0.0,  0.0, 0.0, 0.0, #63
        -0.2, -0.4, 0.0,  0.0, 0.0, 0.0, #64
         0.0, -0.4, 0.0,  0.0, 0.0, 0.0, #65
         0.2, -0.4, 0.0,  0.0, 0.0, 0.0, #66
         0.4, -0.4, 0.0,  0.0, 0.0, 0.0, #67
         0.6, -0.4, 0.0,  0.0, 0.0, 0.0, #68
         0.8, -0.4, 0.0,  0.0, 0.0, 0.0, #69
        -0.8, -0.6, 0.0,  0.0, 0.0, 0.0, #70
        -0.6, -0.6, 0.0,  0.0, 0.0, 0.0, #71
        -0.4, -0.6, 0.0,  0.0, 0.0, 0.0, #72
        -0.2, -0.6, 0.0,  0.0, 0.0, 0.0, #73
         0.0, -0.6, 0.0,  0.0, 0.0, 0.0, #74
         0.2, -0.6, 0.0,  0.0, 0.0, 0.0, #75
         0.4, -0.6, 0.0,  0.0, 0.0, 0.0, #76
         0.6, -0.6, 0.0,  0.0, 0.0, 0.0, #77
         0.8, -0.6, 0.0,  0.0, 0.0, 0.0, #78
        -0.6, -0.8, 0.0,  0.0, 0.0, 0.0, #79
        -0.4, -0.8, 0.0,  0.0, 0.0, 0.0, #80
        -0.2, -0.8, 0.0,  0.0, 0.0, 0.0, #81
         0.0, -0.8, 0.0,  0.0, 0.0, 0.0, #82
         0.2, -0.8, 0.0,  0.0, 0.0, 0.0, #83
         0.4, -0.8, 0.0,  0.0, 0.0, 0.0, #84
         0.6, -0.8, 0.0,  0.0, 0.0, 0.0, #85
         0.8, -0.8, 0.0,  0.0, 0.0, 0.0 #86
        # It is important to use 32 bits data
        ], dtype = np.float32)
     # Defining connections among vertices
    # We have a triangle every 3 indices specified
    indices = np.array(
        [0, 1, 2,
         2, 3, 0,
         4, 5, 6,
         6, 7, 4,
         16, 17, 9,
         9, 8, 16,
         18, 19, 11,
         11, 10, 18,
         20, 21, 13,
         13, 12, 20,
         22, 23, 15,
         15, 14, 22,
         26, 27, 18,
         18, 17, 26,
         28, 29, 20,
         20, 19, 28,
         30, 31, 22,
         22, 21, 30,
         32, 33, 24,
         24, 23, 32,
         34, 35, 26,
         26, 25, 34,
         36, 37, 28,
         28, 27, 36,
         38, 39, 30,
         30, 29, 38,
         40, 41, 32,
         32, 31, 40,
         44, 45, 36,
         36, 35, 44,
         46, 47, 38,
         38, 37, 46,
         48, 49, 40,
         40, 39, 48,
         50, 51, 42,
         42, 41, 50,
         52, 53, 44,
         44, 43, 52,
         54, 55, 46, 
         46, 45, 54,
         56, 57, 48,
         48, 47, 56,
         58, 59, 50,
         50, 49, 58,
         62, 63, 54,
         54, 53, 62,
         64, 65, 56,
         56, 55, 64,
         66, 67, 58,
         58, 57, 66,
         68, 69, 60,
         60, 59, 68,
         70, 71, 62,
         62, 61, 70,
         72, 73, 64,
         64, 63, 72,
         74, 75, 66,
         66, 65, 74,
         76, 77, 68,
         68, 67, 76,
         79, 80, 72,
         72, 71, 79,
         81, 82, 74,
         74, 73, 81,
         83, 84, 76,
         76, 75, 83,
         85, 86, 78,
         78, 77, 85
         ], dtype= np.uint32)

    size = len(indices)

    # VAO, VBO and EBO and  for the shape
    #####################################
    vao_tablero = glGenVertexArrays(1)
    vbo_tablero = glGenBuffers(1)
    ebo_tablero = glGenBuffers(1)

    # Binding VBO and EBO to the VAO
    glBindVertexArray(vao_tablero)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_tablero)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_tablero)
    glBindVertexArray(0)

    # Setting up stride in the Vertex Attribute Object (VAO)
    #####################################
    glBindVertexArray(vao_tablero)

    # Setting up the location of the attributes position and color from the VBO
    # A vertex attribute has 3 integers for the position (each is 4 bytes),
    # and 3 numbers to represent the color (each is 4 bytes),
    # Henceforth, we have 3*4 + 3*4 = 24 bytes
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 6 * SIZE_IN_BYTES, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)
    
    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 6 * SIZE_IN_BYTES, ctypes.c_void_p(3 * SIZE_IN_BYTES))
    glEnableVertexAttribArray(color)

    # unbinding current vao
    glBindVertexArray(0)

    # Sending vertices and indices to GPU memory
    #####################################
    glBindBuffer(GL_ARRAY_BUFFER, vbo_tablero)
    glBufferData(GL_ARRAY_BUFFER, len(vertexData) * SIZE_IN_BYTES, vertexData, GL_STATIC_DRAW)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_tablero)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(indices) * SIZE_IN_BYTES, indices, GL_STATIC_DRAW)

    return vao_tablero, vbo_tablero, ebo_tablero, size

def createShaderProgram():
    
    # Defining shaders for our pipeline
    vertex_shader = """
    #version 330
    in vec3 position;
    in vec3 color;

    out vec3 fragColor;

    void main()
    {
        fragColor = color;
        gl_Position = vec4(position, 1.0f);
    }
    """

    fragment_shader = """
    #version 330

    in vec3 fragColor;
    out vec4 outColor;

    void main()
    {
        outColor = vec4(fragColor, 1.0f);
    }
    """

    # Binding artificial vertex array object for validation
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # Assembling the shader program (pipeline) with both shaders
    shaderProgram = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    return shaderProgram

def crear_damas(shaderProgram,x,y,r,g,b,radius):
    dama = crear_dama(x,y,r,g,b,radius) 
     # VAO, VBO and EBO and  for the shape
    #####################################
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    ebo = glGenBuffers(1)

    # Binding VBO and EBO to the VAO
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBindVertexArray(0)

    # Setting up stride in the Vertex Attribute Object (VAO)
    #####################################
    glBindVertexArray(vao)

    # Setting up the location of the attributes position and color from the VBO
    # A vertex attribute has 3 integers for the position (each is 4 bytes),
    # and 3 numbers to represent the color (each is 4 bytes),
    # Henceforth, we have 3*4 + 3*4 = 24 bytes
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 6 * SIZE_IN_BYTES, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)
    
    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 6 * SIZE_IN_BYTES, ctypes.c_void_p(3 * SIZE_IN_BYTES))
    glEnableVertexAttribArray(color)

    # unbinding current vao
    glBindVertexArray(0)

    # Sending vertices and indices to GPU memory
    #####################################
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, len(dama) * SIZE_IN_BYTES, dama, GL_STATIC_DRAW)
    

    return vao, vbo, dama

if __name__ == "__main__":
    window=None
    # Initialize glfw
    if not glfw.init():
        glfw.set_window_should_close(window, True)

    width = 600
    height = 600

    window = glfw.create_window(width, height, "Drawing a quad via a EBO", None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)

    glfw.make_context_current(window)

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, on_key)
    
    # Creating our shader program and telling OpenGL to use it
    shaderProgram = createShaderProgram()
    glUseProgram(shaderProgram)

    # Creating shapes on GPU memory
    vao_0, vbo_0, ebo_0, size = crear_Tablero(shaderProgram)
    vao_1, vbo_1, dama_1 = crear_damas(shaderProgram,-0.7, 0.7, 0.0, 0.0, 1.0, 0.04)
    vao_2, vbo_2, dama_2 = crear_damas(shaderProgram, -0.3, 0.7, 0.0, 0.0, 1.0, 0.04)
    vao_3, vbo_3, dama_3 = crear_damas(shaderProgram, 0.1, 0.7, 0.0, 0.0, 1.0, 0.04)
    vao_4, vbo_4, dama_4 = crear_damas(shaderProgram, 0.5, 0.7, 0.0, 0.0, 1.0, 0.04)
    vao_5, vbo_5, dama_5 = crear_damas(shaderProgram,-0.5, 0.5, 0.0, 0.0, 1.0, 0.04)
    vao_6, vbo_6, dama_6 = crear_damas(shaderProgram, -0.1, 0.5, 0.0, 0.0, 1.0, 0.04)
    vao_7, vbo_7, dama_7 = crear_damas(shaderProgram, 0.3, 0.5, 0.0, 0.0, 1.0, 0.04)
    vao_8, vbo_8, dama_8 = crear_damas(shaderProgram, 0.7, 0.5, 0.0, 0.0, 1.0, 0.04)
    vao_9, vbo_9, dama_9 = crear_damas(shaderProgram,-0.7, 0.3, 0.0, 0.0, 1.0, 0.04)
    vao_10, vbo_10, dama_10 = crear_damas(shaderProgram,-0.3, 0.3, 0.0, 0.0, 1.0, 0.04)
    vao_11, vbo_11, dama_11 = crear_damas(shaderProgram,0.1, 0.3, 0.0, 0.0, 1.0, 0.04)
    vao_12, vbo_12, dama_12 = crear_damas(shaderProgram,0.5, 0.3, 0.0, 0.0, 1.0, 0.04)
    vao_13, vbo_13, dama_13 = crear_damas(shaderProgram,-0.5, -0.3, 1.0, 0.0, 0.0, 0.04)
    vao_14, vbo_14, dama_14 = crear_damas(shaderProgram,-0.1, -0.3, 1.0, 0.0, 0.0, 0.04)
    vao_15, vbo_15, dama_15 = crear_damas(shaderProgram,0.3, -0.3, 1.0, 0.0, 0.0, 0.04)
    vao_16, vbo_16, dama_16 = crear_damas(shaderProgram,0.7, -0.3, 1.0, 0.0, 0.0, 0.04)
    vao_17, vbo_17, dama_17 = crear_damas(shaderProgram,-0.7, -0.5, 1.0, 0.0, 0.0, 0.04)
    vao_18, vbo_18, dama_18 = crear_damas(shaderProgram,-0.3, -0.5, 1.0, 0.0, 0.0, 0.04)
    vao_19, vbo_19, dama_19 = crear_damas(shaderProgram,0.1, -0.5, 1.0, 0.0, 0.0, 0.04)
    vao_20, vbo_20, dama_20 = crear_damas(shaderProgram,0.5, -0.5, 1.0, 0.0, 0.0, 0.04)
    vao_21, vbo_21, dama_21 = crear_damas(shaderProgram,-0.5, -0.7, 1.0, 0.0, 0.0, 0.04)
    vao_22, vbo_22, dama_22 = crear_damas(shaderProgram,-0.1, -0.7, 1.0, 0.0, 0.0, 0.04)
    vao_23, vbo_23, dama_23 = crear_damas(shaderProgram,0.3, -0.7, 1.0, 0.0, 0.0, 0.04)
    vao_24, vbo_24, dama_24 = crear_damas(shaderProgram,0.7, -0.7, 1.0, 0.0, 0.0, 0.04)
    # Setting up the clear screen color
    glClearColor(0.15, 0.15, 0.15, 1.0)

    while not glfw.window_should_close(window):
        # Using GLFW to check for input events
        glfw.poll_events()

        # Filling or not the shapes depending on the controller state
        if (controller.fillPolygon):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)
        
        glBindVertexArray(vao_0)
        glDrawElements(GL_TRIANGLES, size, GL_UNSIGNED_INT, None)
        glBindVertexArray(vao_1)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_1)/6))
        glBindVertexArray(vao_2)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_2)/6))
        glBindVertexArray(vao_3)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_3)/6))
        glBindVertexArray(vao_4)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_4)/6))
        glBindVertexArray(vao_5)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_5)/6))
        glBindVertexArray(vao_6)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_6)/6))
        glBindVertexArray(vao_7)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_7)/6))
        glBindVertexArray(vao_8)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_8)/6))
        glBindVertexArray(vao_9)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_9)/6))
        glBindVertexArray(vao_10)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_10)/6))
        glBindVertexArray(vao_11)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_11)/6))
        glBindVertexArray(vao_12)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_12)/6))
        glBindVertexArray(vao_13)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_13)/6))
        glBindVertexArray(vao_14)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_14)/6))
        glBindVertexArray(vao_15)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_15)/6))
        glBindVertexArray(vao_16)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_16)/6))
        glBindVertexArray(vao_17)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_17)/6))
        glBindVertexArray(vao_18)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_18)/6))
        glBindVertexArray(vao_19)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_19)/6))
        glBindVertexArray(vao_20)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_20)/6))
        glBindVertexArray(vao_21)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_21)/6))
        glBindVertexArray(vao_22)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_22)/6))
        glBindVertexArray(vao_23)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_23)/6))
        glBindVertexArray(vao_24)
        glDrawArrays(GL_TRIANGLES, 0, int(len(dama_24)/6))


        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    # freeing GPU memory
    glDeleteBuffers(1, [vbo_0])
    glDeleteBuffers(1, [ebo_0])
    glDeleteVertexArrays(1, [vao_0])
    glDeleteBuffers(1, [vbo_1])
    glDeleteVertexArrays(1, [vao_1])
    glDeleteBuffers(1, [vbo_2])
    glDeleteVertexArrays(1, [vao_2])
    glDeleteBuffers(1, [vbo_3])
    glDeleteVertexArrays(1, [vao_3])
    glDeleteBuffers(1, [vbo_4])
    glDeleteVertexArrays(1, [vao_4])
    glDeleteBuffers(1, [vbo_5])
    glDeleteVertexArrays(1, [vao_5])
    glDeleteBuffers(1, [vbo_6])
    glDeleteVertexArrays(1, [vao_6])
    glDeleteBuffers(1, [vbo_7])
    glDeleteVertexArrays(1, [vao_7])
    glDeleteBuffers(1, [vbo_8])
    glDeleteVertexArrays(1, [vao_8])
    glDeleteBuffers(1, [vbo_9])
    glDeleteVertexArrays(1, [vao_9])
    glDeleteBuffers(1, [vbo_10])
    glDeleteVertexArrays(1, [vao_10])
    glDeleteBuffers(1, [vbo_11])
    glDeleteVertexArrays(1, [vao_11])
    glDeleteBuffers(1, [vbo_12])
    glDeleteVertexArrays(1, [vao_12])
    glDeleteBuffers(1, [vbo_13])
    glDeleteVertexArrays(1, [vao_13])
    glDeleteBuffers(1, [vbo_14])
    glDeleteVertexArrays(1, [vao_14])
    glDeleteBuffers(1, [vbo_15])
    glDeleteVertexArrays(1, [vao_15])
    glDeleteBuffers(1, [vbo_16])
    glDeleteVertexArrays(1, [vao_16])
    glDeleteBuffers(1, [vbo_17])
    glDeleteVertexArrays(1, [vao_17])
    glDeleteBuffers(1, [vbo_18])
    glDeleteVertexArrays(1, [vao_18])
    glDeleteBuffers(1, [vbo_19])
    glDeleteVertexArrays(1, [vao_19])
    glDeleteBuffers(1, [vbo_20])
    glDeleteVertexArrays(1, [vao_20])
    glDeleteBuffers(1, [vbo_21])
    glDeleteVertexArrays(1, [vao_21])
    glDeleteBuffers(1, [vbo_22])
    glDeleteVertexArrays(1, [vao_22])
    glDeleteBuffers(1, [vbo_23])
    glDeleteVertexArrays(1, [vao_23])
    glDeleteBuffers(1, [vbo_24])
    glDeleteVertexArrays(1, [vao_24])
    

    glfw.terminate()
