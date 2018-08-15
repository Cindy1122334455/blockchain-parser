# !/usr/local/bin/ python3.6
import sys
import csv
import os
from blockchain_parser.utils import pubkey_to_address
from blockchain_parser.blockchain import Blockchain

sys.path.append('..')
from blockchain_parser.blockchain import Blockchain
from blockchain_parser.utils import pubkey_to_address
# Instantiate the Blockchain by giving the path to the directory
# containing the .blk files created by bitcoind

def getPkfromOutputScript(scriptStr):
    stack = scriptStr.split()
    for e in stack:
        if not e.startswith('OP'):
            return e
    return ''

def getOutAddr(txOut):
    temp = ""
    for outAddr in txOut.addresses:
        temp += outAddr.address + " "
    return temp.strip()

with open('blockoutput.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['block number','block version', 'previous block hash','current block hash', 'transaction hash','FromAddress', 'ToAddress', '#of coins', 'time-stamp'])
    blockchain = Blockchain(os.path.expanduser('/Users/fanfangege/Library/Application Support/Bitcoin/blocks'))
    for block in blockchain.get_ordered_blocks(os.path.expanduser('/Users/fanfangege/Library/Application Support/Bitcoin/blocks/index'), start=200000, end=200010):
        print("height=%d block=%s" % (block.height, block.hash))
        for transaction in block.transactions:
            print("transaction hash: " + transaction.hash)
            fromAddr = ""
            for txIn in transaction.inputs:
                try:
                    if transaction.is_coinbase():
                        fromAddr += "coinbase transaction" + "|"
                    elif str(txIn.script.publicKeyAddress) == "":
                        fromAddr += "Unparsed address" + "|"
                    else:
                        fromAddr += str(txIn.script.publicKeyAddress) + "|"
                    print("fromAddress :" + fromAddr)

                except:
                    fromAddr += "Unable to decode input address" + "|"
                    print("fromAddress :" + fromAddr)
                    pass
            toAddr = ""
            spentValue = ""
            for txOut in transaction.outputs:
                try:
                    toAddr += getOutAddr(txOut) + "|"
                    spentValue += str(txOut.value) + "|"
                    print("toAddress :" + toAddr)
                
                except:
                    toAddr += "Unable to decode input address" + "|"
                    spentValue += "" + "|"
                    print("toAddress :" + toAddr)
                    pass

            spamwriter.writerow([block.height,block.header.version, block.header.previous_block_hash,block.hash,
                transaction.hash, fromAddr.strip('|'), toAddr.strip('|'),spentValue.strip('|'), block.header.timestamp])



#blockchain = Blockchain("/Users/fanfangege/Desktop/python-bitcoin-blockchain-parser/blk00000.dat")

# To get the blocks ordered by height, you need to provide the path of the
# `index` directory (LevelDB index) being maintained by bitcoind. It contains
# .ldb files and is present inside the `blocks` directory
#for block in blockchain.get_ordered_blocks(sys.argv[1] + '/index', end=1000):
    #print("height=%d block=%s" % (block.height, block.hash))

