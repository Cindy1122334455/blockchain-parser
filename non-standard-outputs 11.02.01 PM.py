# Copyright (C) 2015-2016 The bitcoin-blockchain-parser developers
#
# This file is part of bitcoin-blockchain-parser.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of bitcoin-blockchain-parser, including this file, may be copied,
# modified, propagated, or distributed except according to the terms contained
# in the LICENSE file.

# !/usr/local/bin/ python3.6
import sys
import csv
import os
sys.path.append('..')
from blockchain_parser.blockchain import Blockchain
from blockchain_parser.utils import pubkey_to_address
with open('blockoutput.csv', 'w') as csvfile:   #write a csv file to store data
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['block-version', 'previous block hash', 'merkle root', 'blockheader-bits', 'blockheader-nonce',
    'blockheader-difficulty','current block hash', 'transaction hash','fromAddress', 'ToAddress', '#of coins', 'time-stamp'])
    blockchain = Blockchain(os.path.expanduser('/Users/fanfangege/Desktop/blocks'))
    height = 0
    for block in blockchain.get_unordered_blocks():
        block.height = height

        print("height=%d block=%s" % (block.height, block.hash))
        print(block.header.timestamp)
        for transaction in block.transactions:
            print("transaction hash: " + transaction.hash)
            for txIn in transaction.inputs:
                if transaction.is_coinbase():
                    fromAddr = ""
                else:
                    fromAddr = str(txIn.script.publicKeyAddress)
                print("fromAddress :" + fromAddr)
                for txOut in transaction.outputs:
                    for outAddr in txOut.addresses:
                        print("ToAddress :" + outAddr.address)
                        spamwriter.writerow(
                            [block.header.version, block.header.previous_block_hash, block.header.merkle_root,block.header.bits, block.header.nonce,
                             block.header.difficulty,block.hash,transaction.hash,fromAddr, outAddr.address,txOut.value, block.header.timestamp])
                        for output in transaction.outputs:
                            if output.is_unknown():
                               print(block.header.timestamp, output.script.value)
        height = height + 1
