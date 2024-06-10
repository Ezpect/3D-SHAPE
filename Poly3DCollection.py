import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set display dimensions
display_width = 800
display_height = 600

# Initialize OpenGL
glViewport(0, 0, display_width, display_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display_width/display_height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

# Function to draw a cube
def draw_cube(position=(0, 0, 0), size=1, color=(1, 1, 1)):
    x, y, z = position
    half_size = size / 2
    glColor3f(*color)
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(x - half_size, y - half_size, z + half_size)
    glVertex3f(x + half_size, y - half_size, z + half_size)
    glVertex3f(x + half_size, y + half_size, z + half_size)
    glVertex3f(x - half_size, y + half_size, z + half_size)
    # Back face
    glVertex3f(x - half_size, y - half_size, z - half_size)
    glVertex3f(x + half_size, y - half_size, z - half_size)
    glVertex3f(x + half_size, y + half_size, z - half_size)
    glVertex3f(x - half_size, y + half_size, z - half_size)
    # Left face
    glVertex3f(x - half_size, y - half_size, z - half_size)
    glVertex3f(x - half_size, y - half_size, z + half_size)
    glVertex3f(x - half_size, y + half_size, z + half_size)
    glVertex3f(x - half_size, y + half_size, z - half_size)
    # Right face
    glVertex3f(x + half_size, y - half_size, z - half_size)
    glVertex3f(x + half_size, y - half_size, z + half_size)
    glVertex3f(x + half_size, y + half_size, z + half_size)
    glVertex3f(x + half_size, y + half_size, z - half_size)
    # Top face
    glVertex3f(x - half_size, y + half_size, z - half_size)
    glVertex3f(x + half_size, y + half_size, z - half_size)
    glVertex3f(x + half_size, y + half_size, z + half_size)
    glVertex3f(x - half_size, y + half_size, z + half_size)
    # Bottom face
    glVertex3f(x - half_size, y - half_size, z - half_size)
    glVertex3f(x + half_size, y - half_size, z - half_size)
    glVertex3f(x + half_size, y - half_size, z + half_size)
    glVertex3f(x - half_size, y - half_size, z + half_size)
    glEnd()

# Function to draw a sphere
def draw_sphere(position=(0, 0, 0), radius=1, color=(1, 1, 1)):
    x, y, z = position
    glColor3f(*color)
    glPushMatrix()
    glTranslatef(x, y, z)
    quad = gluNewQuadric()
    gluSphere(quad, radius, 20, 20)
    glPopMatrix()

# Function to draw a pyramid
def draw_pyramid(position=(0, 0, 0), size=1, color=(1, 1, 1)):
    x, y, z = position
    half_size = size / 2
    height = size
    
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    # Front face
    glVertex3f(x, y + height, z)
    glVertex3f(x - half_size, y, z + half_size)
    glVertex3f(x + half_size, y, z + half_size)
    # Right face
    glVertex3f(x, y + height, z)
    glVertex3f(x + half_size, y, z + half_size)
    glVertex3f(x + half_size, y, z - half_size)
    # Back face
    glVertex3f(x, y + height, z)
    glVertex3f(x + half_size, y, z - half_size)
    glVertex3f(x - half_size, y, z - half_size)
    # Left face
    glVertex3f(x, y + height, z)
    glVertex3f(x - half_size, y, z - half_size)
    glVertex3f(x - half_size, y, z + half_size)
    glEnd()
    glBegin(GL_QUADS)
    # Bottom face
    glVertex3f(x - half_size, y, z + half_size)
    glVertex3f(x + half_size, y, z + half_size)
    glVertex3f(x + half_size, y, z - half_size)
    glVertex3f(x - half_size, y, z - half_size)
    glEnd()

# Main function
def main():
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Clear the screen and depth buffer
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # Reset model view matrix
        glLoadIdentity()
        
        # Move objects away from camera
        glTranslatef(0, 0, -5)
        
        # Rotate objects
        glRotatef(1, 3, 1, 1)
        
        # Draw objects
        draw_cube(position=(-1, -1, -1), size=1, color=(1, 0, 0))
        draw_sphere(position=(2, 0, 0), radius=1, color=(0, 1, 0))
        draw_pyramid(position=(0, 2, 0), size=1, color=(0, 0, 1))
        
        # Swap buffers
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
