# connect-4-AI
based on minimax algorithm with aplha-beta prunning
<br/>
Implementation of Connect 4 game with AI.<br /><br />
![alt text](https://github.com/imajit/connect-4-AI/blob/master/connect4.jpeg)<br /><br />
In the original state all the places in the board are empty denoted by 0 in each place.The player-pieces are denoted by 1 and the AI-pieces are denoted by 2
![alt text](https://github.com/imajit/connect-4-AI/blob/master/original_state.png)<br /><br />
As the game proceeds the player has to choose a column from 0 to size of board - 1 and put his piece there . If its a valid move then AI also places its piece. The game continues till any of the 2 players get 4 of his pieces in a row horizontally, vertically or diagonally.
![alt text](https://github.com/imajit/connect-4-AI/blob/master/win_state.png)<br/><br/>
<b>Features </b><br/>
1. Terminal based game - works completely on terminal <br/>
2. Depth 4 Minimax tree is generated to find next best move<br/>
3. Algorithm is optomized by alpha-beta prunning <br/>
<b>Future Advancements</b><br/>
1. Gui can be added to make game more interesting.<br/>
2. Depth of tree can be increased to get better results.<br/>
3. Better and more detailed scoring can improve the results.<br/>
