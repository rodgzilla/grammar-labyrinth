from enum import Enum

Directions = Enum('Directions', 'N S E W')
opposite_direction = {
                      Directions.N : Directions.S, Directions.S : Directions.N, 
                      Directions.W : Directions.E, Directions.E : Directions.W
                     }

