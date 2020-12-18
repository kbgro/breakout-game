# The **Breakout** _game_

The breakout game starts with a `paddle` and a `ball` at the bottom of the screen and some rows of `bricks` at the top. The player **must** eliminate all the bricks by hitting them with a `ball`, which _rebounds_ against the borders of the screen, the `bricks`, and the bottom `paddle`.

>The player controls the horizontal movement of the `paddle`.

The player **starts the game** with 3 lives, and if they miss the ball's rebound and it reaches the bottom border of the screen, one of the life is lost.

The **game is over** when;
- all the bricks are destroyed, or when
- the player losses all lives.


## play
```bash
python -m breakout
```
