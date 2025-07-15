import game

# Initialize the game with the USER agent
# This agent allows you to play manually by pressing SPACE
g = game.Game(agent_name="user_agent", device="cpu")

# Run the game, drawing it to the screen
g.main(draw=True)