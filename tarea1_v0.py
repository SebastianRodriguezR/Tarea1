import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy
import sys

__author__ = "Ivan Sipiran"
__license__ = "MIT"

# We will use 32 bits data, so an integer has 4 bytes
# 1 byte = 8 bits
SIZE_IN_BYTES = 4

def crear_dama(x,y,r,g,b,radius):
    
    circle = []
    for angle in range(0,360,10):
        circle.extend([x, y, 0.0, r, g, b])
        circle.extend([x+numpy.cos(numpy.radians(angle))*radius, 
                       y+numpy.sin(numpy.radians(angle))*radius, 
                       0.0, r, g, b])
        circle.extend([x+numpy.cos(numpy.radians(angle+10))*radius, 
                       y+numpy.sin(numpy.radians(angle+10))*radius, 
                       0.0, r, g, b])
    
    return numpy.array(circle, dtype = numpy.float32)

if __name__ == "__main__":
    window=None
    # Initialize glfw
    if not glfw.init():
        glfw.set_window_should_close(window, True)

    width = 600
    height = 600

    window = glfw.create_window(width, height, "Tarea 1", None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)

    glfw.make_context_current(window)

    dama_1 = crear_dama(-0.7, 0.7, 0.0, 0.0, 1.0, 0.04)
    dama_2 = crear_dama(-0.3, 0.7, 0.0, 0.0, 1.0, 0.04)
    dama_3 = crear_dama(0.1, 0.7, 0.0, 0.0, 1.0, 0.04)
    dama_4 = crear_dama(0.5, 0.7, 0.0, 0.0, 1.0, 0.04)
    dama_5 = crear_dama(-0.5, 0.5, 0.0, 0.0, 1.0, 0.04)
    dama_6 = crear_dama(-0.1, 0.5, 0.0, 0.0, 1.0, 0.04)
    dama_7 = crear_dama(0.3, 0.5, 0.0, 0.0, 1.0, 0.04)
    dama_8 = crear_dama(0.7, 0.5, 0.0, 0.0, 1.0, 0.04)
    dama_9 = crear_dama(-0.7, 0.3, 0.0, 0.0, 1.0, 0.04)
    dama_10 = crear_dama(-0.3, 0.3, 0.0, 0.0, 1.0, 0.04)
    dama_11 = crear_dama(0.1, 0.3, 0.0, 0.0, 1.0, 0.04)
    dama_12 = crear_dama(0.5, 0.3, 0.0, 0.0, 1.0, 0.04)
    dama_13 = crear_dama(-0.5, -0.3, 1.0, 0.0, 0.0, 0.04)
    dama_14 = crear_dama(-0.1, -0.3, 1.0, 0.0, 0.0, 0.04)
    dama_15 = crear_dama(0.3, -0.3, 1.0, 0.0, 0.0, 0.04)
    dama_16 = crear_dama(0.7, -0.3, 1.0, 0.0, 0.0, 0.04)
    dama_17 = crear_dama(-0.7, -0.5, 1.0, 0.0, 0.0, 0.04)
    dama_18 = crear_dama(-0.3, -0.5, 1.0, 0.0, 0.0, 0.04)
    dama_19 = crear_dama(0.1, -0.5, 1.0, 0.0, 0.0, 0.04)
    dama_20 = crear_dama(0.5, -0.5, 1.0, 0.0, 0.0, 0.04)
    dama_21 = crear_dama(-0.5, -0.7, 1.0, 0.0, 0.0, 0.04)
    dama_22 = crear_dama(-0.1, -0.7, 1.0, 0.0, 0.0, 0.04)
    dama_23 = crear_dama(0.3, -0.7, 1.0, 0.0, 0.0, 0.04)
    dama_24 = crear_dama(0.7, -0.7, 1.0, 0.0, 0.0, 0.04)

    # Defining shaders for our pipeline
    vertex_shader = """
    #version 330
    in vec3 position;
    in vec3 color;

    out vec3 newColor;
    void main()
    {
        gl_Position = vec4(position, 1.0f);
        newColor = color;
    }
    """

    fragment_shader = """
    #version 330
    in vec3 newColor;

    out vec4 outColor;
    void main()
    {
        outColor = vec4(newColor, 1.0f);
    }
    """

    # Binding artificial vertex array object for validation
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # Assembling the shader program (pipeline) with both shaders
    shaderProgram = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    # Each shape must be attached to a Vertex Buffer Object (VBO)
    vboDama_1 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_1)
    glBufferData(GL_ARRAY_BUFFER, len(dama_1) * SIZE_IN_BYTES, dama_1, GL_STATIC_DRAW)

    vboDama_2 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_2)
    glBufferData(GL_ARRAY_BUFFER, len(dama_2) * SIZE_IN_BYTES, dama_2, GL_STATIC_DRAW)

    vboDama_3 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_3)
    glBufferData(GL_ARRAY_BUFFER, len(dama_3) * SIZE_IN_BYTES, dama_3, GL_STATIC_DRAW)

    vboDama_4 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_4)
    glBufferData(GL_ARRAY_BUFFER, len(dama_4) * SIZE_IN_BYTES, dama_4, GL_STATIC_DRAW)

    vboDama_5 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_5)
    glBufferData(GL_ARRAY_BUFFER, len(dama_5) * SIZE_IN_BYTES, dama_5, GL_STATIC_DRAW)

    vboDama_6 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_6)
    glBufferData(GL_ARRAY_BUFFER, len(dama_6) * SIZE_IN_BYTES, dama_6, GL_STATIC_DRAW)

    vboDama_7 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_7)
    glBufferData(GL_ARRAY_BUFFER, len(dama_7) * SIZE_IN_BYTES, dama_7, GL_STATIC_DRAW)

    vboDama_8 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_8)
    glBufferData(GL_ARRAY_BUFFER, len(dama_8) * SIZE_IN_BYTES, dama_8, GL_STATIC_DRAW)

    vboDama_9 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_9)
    glBufferData(GL_ARRAY_BUFFER, len(dama_9) * SIZE_IN_BYTES, dama_9, GL_STATIC_DRAW)

    vboDama_10 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_10)
    glBufferData(GL_ARRAY_BUFFER, len(dama_10) * SIZE_IN_BYTES, dama_10, GL_STATIC_DRAW)

    vboDama_11 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_11)
    glBufferData(GL_ARRAY_BUFFER, len(dama_11) * SIZE_IN_BYTES, dama_11, GL_STATIC_DRAW)

    vboDama_12 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_12)
    glBufferData(GL_ARRAY_BUFFER, len(dama_12) * SIZE_IN_BYTES, dama_12, GL_STATIC_DRAW)

    vboDama_13 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_13)
    glBufferData(GL_ARRAY_BUFFER, len(dama_13) * SIZE_IN_BYTES, dama_13, GL_STATIC_DRAW)

    vboDama_14 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_14)
    glBufferData(GL_ARRAY_BUFFER, len(dama_14) * SIZE_IN_BYTES, dama_14, GL_STATIC_DRAW)

    vboDama_15 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_15)
    glBufferData(GL_ARRAY_BUFFER, len(dama_15) * SIZE_IN_BYTES, dama_15, GL_STATIC_DRAW)

    vboDama_16 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_16)
    glBufferData(GL_ARRAY_BUFFER, len(dama_16) * SIZE_IN_BYTES, dama_16, GL_STATIC_DRAW)

    vboDama_17 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_17)
    glBufferData(GL_ARRAY_BUFFER, len(dama_17) * SIZE_IN_BYTES, dama_17, GL_STATIC_DRAW)

    vboDama_18 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_18)
    glBufferData(GL_ARRAY_BUFFER, len(dama_18) * SIZE_IN_BYTES, dama_18, GL_STATIC_DRAW)

    vboDama_19 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_19)
    glBufferData(GL_ARRAY_BUFFER, len(dama_19) * SIZE_IN_BYTES, dama_19, GL_STATIC_DRAW)

    vboDama_20 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_20)
    glBufferData(GL_ARRAY_BUFFER, len(dama_20) * SIZE_IN_BYTES, dama_20, GL_STATIC_DRAW)

    vboDama_21 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_21)
    glBufferData(GL_ARRAY_BUFFER, len(dama_21) * SIZE_IN_BYTES, dama_21, GL_STATIC_DRAW)

    vboDama_22 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_22)
    glBufferData(GL_ARRAY_BUFFER, len(dama_22) * SIZE_IN_BYTES, dama_22, GL_STATIC_DRAW)

    vboDama_23 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_23)
    glBufferData(GL_ARRAY_BUFFER, len(dama_23) * SIZE_IN_BYTES, dama_23, GL_STATIC_DRAW)

    vboDama_24 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboDama_24)
    glBufferData(GL_ARRAY_BUFFER, len(dama_24) * SIZE_IN_BYTES, dama_24, GL_STATIC_DRAW)

    # Telling OpenGL to use our shader program
    glUseProgram(shaderProgram)

    # Setting up the clear screen color
    glClearColor(0.5,0.5, 0.5, 1.0)

    glClear(GL_COLOR_BUFFER_BIT)

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_1)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_1)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_2)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_2)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_3)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_3)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_4)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_4)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_5)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_5)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_6)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_6)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_7)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_7)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_8)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_8)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_9)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_9)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_10)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_10)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_11)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_11)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_12)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_12)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_13)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_13)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_14)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_14)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_15)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_15)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_16)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_16)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_17)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_17)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_18)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_18)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_19)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_19)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_20)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_20)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_21)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_21)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_22)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_22)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_23)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_23)/6))

    glBindBuffer(GL_ARRAY_BUFFER, vboDama_24)
    position = glGetAttribLocation(shaderProgram, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shaderProgram, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)
    glDrawArrays(GL_TRIANGLES, 0, int(len(dama_24)/6))

    # Moving our draw to the active color buffer
    glfw.swap_buffers(window)

    # Waiting to close the window
    while not glfw.window_should_close(window):

        # Getting events from GLFW
        glfw.poll_events()
        
    glfw.terminate()