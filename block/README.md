## Block mining

This code takes as input Index of block, Hash of the parent block, Target and Block body file and finds a nonce and 
timestamp to get the sha256 hash of the block less than the specified target.

#### Sample data:
Index: 5       
Hash of parent block: 2b21ef8ab698e7daf03ccf0110acb4d844fabb5b9513221285f96593d4d4a573      
Target: 0000000f00000000000000000000000000000000000000000000000000000000       
Block body: 015.dat

Times taken to find nonce:
* 6m
* 0m 40s
* 8m 2s
* 5m 50s
