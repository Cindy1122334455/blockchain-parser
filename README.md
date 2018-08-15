# python-blockchain-parser
Our parsing codes was inspired by Antoine Le Calvez "https://github.com/alecalve/python-bitcoin-blockchain-parser" and we really appreciated his contribution on the parsing tool. We made some adjustments on his codes according to our needs for extracting all the blocks from the very beginning till the latest block and then created our own database comprising of  "block number, block version, previous block hash, current block hash , transaction hash, From Address,  To Address, value of coins, time stamp", which are really important variables in blockchain data in order to make further analysis on blockchain and social network analysis. When running all the codes, we are able to obtain all the blockchain data saved in the csv file. We also took consideration into several situations in "From Address" and "To Address" such as " coinbase transaction", "Unparsed address", "Unable to decode input address" , which needs to be treated carefully in further analysis and visualization.

Our codes support Python 3. So When you run it , you'd better type "python3 " in the terminal in case that there are two versions of python in the machine.

## Downloading bitcoin client
Downloading Bitcoin Core from "https://bitcoin.org/en/bitcoin-core/" to catch up to the latest block and then we are able to use Bitcoin Core's LevelDB index to locate ordered block data in its .blk files.

## Installing some required packages before running codes
Requirements : python-bitcoinlib, plyvel, coverage for tests
plyvel requires leveldb development libraries for LevelDB >1.2.X

On Linux, install libleveldb-dev

``sudo apt-get install libleveldb-dev``

Then, just run

``  python setup.py install   ``

## Steps about starting running codes
1. Open  "ordered-blocks.py" and then modify the statement " blockchain = Blockchain(os.path.expanduser('/Users/fanfangege/Library/Application Support/Bitcoin/blocks'))" according to the directory of "/Bitcoin/blocks" in your own machine.
2. Modify the statement "for block in blockchain.get_ordered_blocks(os.path.expanduser('/Users/fanfangege/Library/Application Support/Bitcoin/blocks/index'), start= , end= ):" according to the current directory of "Bitcoin/blocks/index" (which might be "~/.bitcoin/blocks/index" in Linux System) in your own machine. And then you are free to specify the arbitrary starting and ending block according to the height of block in the Bitcoin Core. The very first block height starts with "0" and you can modify the the number of "end" as the number of latest blocks in the Bitcoin Core which can be checked via looking up to the bottle right corner of Bitcoin Core with the symbol of "check mark".
3. After all the above steps being done, kill the Bitcoin Core since it only allows one processor having a control on the levelDB database.
4. Input "python3 ordered-blocks.py" in terminal to run all the codes.

