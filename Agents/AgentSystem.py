# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
import pygame
import random
import math
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
 
# This class represents the ball        
# It derives from the "Sprite" class in Pygame
class Agent(pygame.sprite.Sprite):
    
    left_boundary = 0
    right_boundary = 0
    top_boundary = 0
    bottom_boundary = 0
    change_x = 0
    change_y = 0
    Attack=0
    Direction=200
    walls=None
    # Constructor. Pass in the color of the agent, 
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        # Create an image of the agent, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
    def bounce(self,diff):
        self.Direction=(180-self.direction) % 360
        self.Direction-=diff

    # Called each frame
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
            
        block_hit_list=pygame.spritecollide(self,self.walls,False)
        for block in block_hit_list:
            if self.change_y>0
                self..rect.bottom=block.rect.top
            else:
                self.rect.top=block.rect.bottom

                
#class Oppenent_Agent(Agent):
    
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])
 
# This is a list of 'sprites.' Each agent in the program is
# added to this list. The list is managed by a class called 'Group.'
agent_list = pygame.sprite.Group()
agent_Kill_list = pygame.sprite.Group()
# This is a list of every sprite. All agents and the player agent as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(10):
    # This represents a agent
    agent = Agent(red, 20, 15)
 
    # Set a random location for the agent
    agent.rect.x = random.randrange(screen_width)
    agent.rect.y = random.randrange(screen_height)
    
    agent.change_x = random.randrange(-3,4)
    agent.change_y = random.randrange(-3,4)
    agent.left_boundary = 0
    agent.top_boundary = 0
    agent.right_boundary = screen_width
    agent.bottom_boundary = screen_height
    agent.Attack=random.randrange(1,10)
    
    # Add the agent to the list of objects
    agent_list.add(agent)
    all_sprites_list.add(agent)
    agent.walls=all_sprites_list;
     
for i in range(10):
    # This represents a agent
    agent_Kill = Agent(black, 20, 15)
 
    # Set a random location for the agent
    agent_Kill.rect.x = random.randrange(screen_width)
    agent_Kill.rect.y = random.randrange(screen_height)
    
    agent_Kill.change_x = random.randrange(-3,4)
    agent_Kill.change_y = random.randrange(-3,4)
    agent_Kill.left_boundary = 0
    agent_Kill.top_boundary = 0
    agent_Kill.right_boundary = screen_width
    agent_Kill.bottom_boundary = screen_height
    agent_Kill.Attack=random.randrange(1,10)
    # Add the agent to the list of objects
    agent_Kill_list.add(agent_Kill)
    all_sprites_list.add(agent_Kill)     
    agent_Kill.walls=all_sprites_list

 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # Clear the screen
    screen.fill(white)
    
    # Calls update() method on every sprite in the list
    all_sprites_list.update()
    # See if the player agent has collided with anything.
    agent_hit_Kill_list=pygame.sprite.spritecollide(agent_Kill,agent_list,False)

		
    # Draw all the spites
    all_sprites_list.draw(screen)
     
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
