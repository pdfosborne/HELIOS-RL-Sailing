# HELIOS-RL-Sailing

Application of the HELIOS-RL system to a Sailing Simulator.

HELIOS-RL
https://github.com/pdfosborne/HELIOS-RL

Sailing Simulator:
 - https://github.com/topics/sailing-simulator
 - Simple sailing simulator from https://github.com/PPierzc/ai-learns-to-sail
   - https://github.com/PPierzc/ai-learns-to-sail/blob/master/tasks/channel.py

If setup correctly then the rest is handled by the HELIOS system
> Run main.py (change experiment call and parameters as needed)

# Instruction following

### Instruction: Descriptions
- dead center from left/right: dead center of the river
  NEW -> center from left/right: move to the middle of the river

V2.1:
- beach side: continue so that the boat is on the beach side near the middle of the river with the wind on the port side
- turn back from beach: when on the beach side and in between the edge and the center of the river, turn back towards the center so the wind is on the starboard side
- harbor side: continue so that the boat is on the harbor side near the middle of the river with the wind on the starboard side
- turn back from harbor: when on the harbor side and in between the edge and the center of the river, turn back towards the center so the wind is on the port side

V2.2:
- beach side: continue so that the boat is near the center of the river but on the beach side with the wind on the port side of the boat
- turn back from beach: when halfway between the center and the edge of the river on the beach side, turn back towards the center so the wind is on the starboard side
- harbor side: continue so that the boat is near the center of the river but on the harbor side with the wind on the starboard side of the boat
- turn back from harbor: when halfway between the center and the edge of the river on the harbor side, turn back towards the center so the wind is on the port side
- middle: move to the middle of the river

V2.3:
- beach side: continue so that the boat is halfway between the center and the edge of the river but on the beach side with the wind on the port side of the boat
- turn back from beach: when the boat is halfway between the center and the edge of the river on the beach side, turn back towards the center so the wind is on the starboard side








