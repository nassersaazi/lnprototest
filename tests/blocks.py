#! /usr/bin/python3
from lnprototest import Block

# BLOCK_102 allows funding of channels with several UTXOs for easy testing.
#
# Here are the keys to spend funds, derived from BIP32 seed
# `0000000000000000000000000000000000000000000000000000000000000001`:
#
#    pubkey 0/0/1: 02d6a3c2d0cf7904ab6af54d7c959435a452b24a63194e1c4e7c337d3ebbb3017b
#    privkey 0/0/1: 76edf0c303b9e692da9cb491abedef46ca5b81d32f102eb4648461b239cb0f99
#    WIF 0/0/1: cRZtHFwyrV3CS1Muc9k4sXQRDhqA1Usgi8r7NhdEXLgM5CUEZufg
#    P2WPKH 0/0/1: bcrt1qsdzqt93xsyewdjvagndw9523m27e52er5ca7hm
#    UTXO: 16835ac8c154b616baac524163f41fb0c4f82c7b972ad35d4d6f18d854f6856b/1 (0.01BTC)
#
#    pubkey 0/0/2: 038f1573b4238a986470d250ce87c7a91257b6ba3baf2a0b14380c4e1e532c209d
#    privkey 0/0/2: bc2f48a76a6b8815940accaf01981d3b6347a68fbe844f81c50ecbadf27cd179
#    WIF 0/0/2: cTtWRYC39drNzaANPzDrgoYsMgs5LkfE5USKH9Kr9ySpEEdjYt3E
#    P2WPKH 0/0/2: bcrt1qlkt93775wmf33uacykc49v2j4tayn0yj25msjn
#    UTXO: 16835ac8c154b616baac524163f41fb0c4f82c7b972ad35d4d6f18d854f6856b/0 (0.02BTC)
#
#    pubkey 0/0/3: 02ffef0c295cf7ca3a4ceb8208534e61edf44c606e7990287f389f1ea055a1231c
#    privkey 0/0/3: 16c5027616e940d1e72b4c172557b3b799a93c0582f924441174ea556aadd01c
#    WIF 0/0/3: cNLxnoJSQDRzXnGPr4ihhy2oQqRBTjdUAM23fHLHbZ2pBsNbqMwb
#    P2WPKH 0/0/3: bcrt1q2ng546gs0ylfxrvwx0fauzcvhuz655en4kwe2c
#    UTXO: 16835ac8c154b616baac524163f41fb0c4f82c7b972ad35d4d6f18d854f6856b/3 (0.03BTC)
#
#    pubkey 0/0/4: 026957e53b46df017bd6460681d068e1d23a7b027de398272d0b15f59b78d060a9
#    privkey 0/0/4: 53ac43309b75d9b86bef32c5bbc99c500910b64f9ae089667c870c2cc69e17a4
#    WIF 0/0/4: cQPMJRjxse9i1jDeCo8H3khUMHYfXYomKbwF5zUqdPrFT6AmtTbd
#    P2WPKH 0/0/4: bcrt1qrdpwrlrmrnvn535l5eldt64lxm8r2nwkv0ruxq
#    UTXO: 16835ac8c154b616baac524163f41fb0c4f82c7b972ad35d4d6f18d854f6856b/4 (0.04BTC)
#
#    pubkey 0/0/5: 03a9f795ff2e4c27091f40e8f8277301824d1c3dfa6b0204aa92347314e41b1033
#    privkey 0/0/5: 16be98a5d4156f6f3af99205e9bc1395397bca53db967e50427583c94271d27f
#    WIF 0/0/5: cNLuxyjvR6ga2q6fdmSKxAd1CPQDShKV9yoA7zFKT7GJwZXr9MmT
#    P2WPKH 0/0/5: bcrt1q622lwmdzxxterumd746eu3d3t40pq53p62zhlz
#    UTXO: 16835ac8c154b616baac524163f41fb0c4f82c7b972ad35d4d6f18d854f6856b/2 (49.89995320BTC)

BLOCK_102 = Block(blockheight=102, txs=['020000000001017b8705087f9bddd2777021d2a1dfefc2f1c5afa833b5c4ab00ccc8a556d042830000000000feffffff0580841e0000000000160014fd9658fbd476d318f3b825b152b152aafa49bc9240420f000000000016001483440596268132e6c99d44dae2d151dabd9a2b2338496d2901000000160014d295f76da2319791f36df5759e45b15d5e105221c0c62d000000000016001454d14ae910793e930d8e33d3de0b0cbf05aa533300093d00000000001600141b42e1fc7b1cd93a469fa67ed5eabf36ce354dd6024730440220782128cb0319a8430a687c51411e34cfaa6641da9a8f881d8898128cb5c46897022056e82d011a95fd6bcb6d0d4f10332b0b0d1227b2c4ced59e540eb708a4b24e4701210279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f8179865000000'])

# Funding tx spending 16835ac8c154b616baac524163f41fb0c4f82c7b972ad35d4d6f18d854f6856b/1, feerate 253 to bitcoin privkeys 0000000000000000000000000000000000000000000000000000000000000010 and 0000000000000000000000000000000000000000000000000000000000000020 (txid 189c40b0728f382fe91c87270926584e48e0af3a6789f37454afee6c756031
BLOCK_103_to_108 = Block(blockheight=103,
                         number=6,
                         txs=['020000000001016b85f654d8186f4d5dd32a977b2cf8c4b01ff4634152acba16b654c1c85a83160100000000ffffffff01c5410f0000000000220020c46bf3d1686d6dbb2d9244f8f67b90370c5aa2747045f1aeccb77d8187117382024730440220798d96d5a057b5b7797988a855217f41af05ece3ba8278366e2f69763c72e785022065d5dd7eeddc0766ddf65557c92b9c52c301f23f94d2cf681860d32153e6ae1e012102d6a3c2d0cf7904ab6af54d7c959435a452b24a63194e1c4e7c337d3ebbb3017b00000000'])

# # This channel claimed by nodeids with privkeys ...002 and ...003.
# CHAN_ANN_103x1x0 = Msg('channel_announcement',
#                        node_signature_1=Sig('02', '4ad0946fa8c3996015dec325c4b0540299287427ec8d8313842ce6f8dc06791a'),
#                        node_signature_2=Sig('03', '4ad0946fa8c3996015dec325c4b0540299287427ec8d8313842ce6f8dc06791a'),
#                        bitcoin_signature_1=Sig('20', '4ad0946fa8c3996015dec325c4b0540299287427ec8d8313842ce6f8dc06791a'),
#                        bitcoin_signature_2=Sig('20', '4ad0946fa8c3996015dec325c4b0540299287427ec8d8313842ce6f8dc06791a'),
#                        features='',
#                        chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                        short_channel_id='103x1x0',
#                        node_id_1='02c6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5',
#                        node_id_2='02f9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f9',
#                        bitcoin_key_1='03e60fce93b59e9ec53011aabc21c23e97b2a31369b87a5ae9c44ee89e2a6dec0a',
#                        bitcoin_key_2='03d30199d74fb5a22d47b6e054e2f378cedacffcb89904a61d75d0dbd407143e65')

# CHAN_UPDATE_103x1x0_002 = Msg('channel_update',
#                               signature=Sig('02', '5133e0542731e0b4b70b4cb99f8fb7dab2e6658b5a5add8d9dfd1a8e2c549f95'),
#                               chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                               short_channel_id='103x1x0',
#                               timestamp=1565587763,
#                               message_flags=0,
#                               channel_flags=0,
#                               cltv_expiry_delta=144,
#                               htlc_minimum_msat=0,
#                               fee_base_msat=1000,
#                               fee_proportional_millionths=10)

# NODE_ANN_002 = Msg('node_announcement',
#                    signature=Sig('02', '511128a78a9a0f1cac973ceb37533497fde5586b54fad3c887d1037195a4ddbd'),
#                    features='',
#                    timestamp=1565587763,
#                    node_id='02c6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5',
#                    rgb_color='02c604',
#                    alias='3032633630343766393434316564376436643330343534303665393563303763',
#                    addresses='01080808082607')

# CHAN_UPDATE_103x1x0_003 = Msg('channel_update',
#                               signature=Sig('03', 'd86dd6f31dc7956bae1e86407f38548fb2cda5f3f7441577694b1c5d455f153f'),
#                               chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                               short_channel_id='103x1x0',
#                               timestamp=1565587763,
#                               message_flags=1,
#                               channel_flags=1,
#                               cltv_expiry_delta=48,
#                               htlc_minimum_msat=0,
#                               fee_base_msat=100,
#                               fee_proportional_millionths=11,
#                               htlc_maximum_msat=100000)

# NODE_ANN_003 = Msg('node_announcement',
#                    signature=Sig('03', '15cf94034b8916d507d90d836f8b2a18b6c513b032714056099fb875db9cec3e'),
#                    features='',
#                    timestamp=1565587763,
#                    node_id='02f9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f9',
#                    rgb_color='02f930',
#                    alias='3032663933303861303139323538633331303439333434663835663839643532',
#                    addresses='0151b6887026070220014c4e1cc141001e6f65fffec8a825260703c43068ceb641d7b25c3a26070441cf248da2034dfa9351a9e946d71ce86f561f50b67753fd8e385d44647bf62cdb91032607')

# # A later node-announcement, a little different.
# NODE_ANN_003_LATER = Msg('node_announcement',
#                          signature=Sig('03', '22de31ba66317a121263102b35cf05fa5c0e5a2100071740428693fa414e9dc5'),
#                          features='',
#                          timestamp=1565597764,
#                          node_id='02f9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f9',
#                          rgb_color='02f930',
#                          alias='3032663933303861303139323538633331303439333434663835663839643532',
#                          addresses='0441cf248da2034dfa9351a9e946d71ce86f561f50b67753fd8e385d44647bf62cdb91032607')

# # Funding tx spending 16835ac8c154b616baac524163f41fb0c4f82c7b972ad35d4d6f18d854f6856b/0, feerate 253 to bitcoin privkeys 0000000000000000000000000000000000000000000000000000000000000030 and 0000000000000000000000000000000000000000000000000000000000000040 (txid db029ee8cc511625887c192c5bb264249fe69b9b86eb627a52f9a313ba231ade)
# BLOCK_109_to_114 = Block(blockheight=109, number=6, txs=['020000000001016b85f654d8186f4d5dd32a977b2cf8c4b01ff4634152acba16b654c1c85a83160000000000ffffffff0105841e0000000000220020fa73be60259cea454ee79a963514f0b7622db62eadc88daafe377bfa2aa30fbb0247304402205735b9750a90be1ca09cdf91d6697bde3746a390698ca754d516b56c72880bae02203c1deef3645cc20e300db1a808ffc7c2f57be200761ee3cf1a479d1e1aef70bc0121038f1573b4238a986470d250ce87c7a91257b6ba3baf2a0b14380c4e1e532c209d00000000'])

# # This channel claimed by nodeids with privkeys ...004 and ...005.
# CHAN_ANN_109x1x0 = Msg('channel_announcement',
#                        node_signature_1=Sig('05', 'dd64b4844ef9728c2486f9bf71273070941f68e4047e8420d764b8e543a2841b'),
#                        node_signature_2=Sig('04', 'dd64b4844ef9728c2486f9bf71273070941f68e4047e8420d764b8e543a2841b'),
#                        bitcoin_signature_1=Sig('40', 'dd64b4844ef9728c2486f9bf71273070941f68e4047e8420d764b8e543a2841b'),
#                        bitcoin_signature_2=Sig('30', 'dd64b4844ef9728c2486f9bf71273070941f68e4047e8420d764b8e543a2841b'),
#                        features='',
#                        chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                        short_channel_id='109x1x0',
#                        node_id_1='022f8bde4d1a07209355b4a7250a5c5128e88b84bddc619ab7cba8d569b240efe4',
#                        node_id_2='02e493dbf1c10d80f3581e4904930b1404cc6c13900ee0758474fa94abe8c4cd13',
#                        bitcoin_key_1='03bf23c1542d16eab70b1051eaf832823cfc4c6f1dcdbafd81e37918e6f874ef8b',
#                        bitcoin_key_2='026eca335d9645307db441656ef4e65b4bfc579b27452bebc19bd870aa1118e5c3')

# CHAN_UPDATE_109x1x0_004 = Msg('channel_update',
#                               signature=Sig('04', 'd0ba981a8ae3f36494765920e7c2b15c823342baa3a594f5013e699d58d75c7d'),
#                               chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                               short_channel_id='109x1x0',
#                               timestamp=1565587764,
#                               message_flags=0,
#                               channel_flags=1,
#                               cltv_expiry_delta=144,
#                               htlc_minimum_msat=0,
#                               fee_base_msat=1000,
#                               fee_proportional_millionths=10)

# NODE_ANN_004 = Msg('node_announcement',
#                    signature=Sig('04', '80307748653b7608ad9932d800581169b4a091de0c5e9084b4d9ff3b96d5d91a'),
#                    features='',
#                    timestamp=1565587764,
#                    node_id='02e493dbf1c10d80f3581e4904930b1404cc6c13900ee0758474fa94abe8c4cd13',
#                    rgb_color='02e493',
#                    alias='3032653439336462663163313064383066333538316534393034393330623134',
#                    addresses='')

# NODE_ANN_004_LATER = Msg('node_announcement',
#                          signature=Sig('04', 'bde4752f90c84e9372c0badf9f0b29a024ed51b623b5f16742f5bb2ca9142f28'),
#                          features='',
#                          timestamp=1565597765,
#                          node_id='02e493dbf1c10d80f3581e4904930b1404cc6c13900ee0758474fa94abe8c4cd13',
#                          rgb_color='02e493',
#                          alias='3032653439336462663163313064383066333538316534393034393330623134',
#                          addresses='')

# CHAN_UPDATE_109x1x0_005 = Msg('channel_update',
#                               signature=Sig('05', '3f698cd8c502919b5bde2cf02ccd7cb5b3023d73dfd2b8d87da3bcc8fa689963'),
#                               chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                               short_channel_id='109x1x0',
#                               timestamp=1565587765,
#                               message_flags=1,
#                               channel_flags=0,
#                               cltv_expiry_delta=48,
#                               htlc_minimum_msat=0,
#                               fee_base_msat=100,
#                               fee_proportional_millionths=11,
#                               htlc_maximum_msat=100000)

# NODE_ANN_005 = Msg('node_announcement',
#                    signature=Sig('05', 'cd127af408247cd7e9eac84e1f723e94a43946616be367c9546db1196b108cbe'),
#                    features='',
#                    timestamp=1565587765,
#                    node_id='022f8bde4d1a07209355b4a7250a5c5128e88b84bddc619ab7cba8d569b240efe4',
#                    rgb_color='022f8b',
#                    alias='3032326638626465346431613037323039333535623461373235306135633531',
#                    addresses='022a03b0c0000300d000000000240020012607')

# # Funding tx spending 16835ac8c154b616baac524163f41fb0c4f82c7b972ad35d4d6f18d854f6856b/3, feerate 253 to bitcoin privkeys 0000000000000000000000000000000000000000000000000000000000000050 and 0000000000000000000000000000000000000000000000000000000000000060 (txid 03330f41079aba9a595310c9c4d78676e5291ee6f1931dd7686f46ed16096186)
# BLOCK_115_to_120 = Block(blockheight=115, number=6, txs=['020000000001016b85f654d8186f4d5dd32a977b2cf8c4b01ff4634152acba16b654c1c85a83160300000000ffffffff0145c62d00000000002200208225164b456194e9721a5ff5ea4df731d3d663f48f3ba96961dc9d0617ea2bf20247304402200bf2e7a300f8d268c9480732748707b36e43f6225f5330eca2cfa00b21c7159a02205390a3469a14b3a48714bb44db6d8ee838ef5e29b3063a32cba22a3a2d4f3e00012102ffef0c295cf7ca3a4ceb8208534e61edf44c606e7990287f389f1ea055a1231c00000000'])

# # This channel claimed by nodeids with privkeys ...003 and ...004.
# CHAN_ANN_115x1x0 = Msg('channel_announcement',
#                        node_signature_1=Sig('04', '4a77eec60b0275f0bdcf1ac572bfd63ff7eaa61050ff54049168e9858279eec0'),
#                        node_signature_2=Sig('03', '4a77eec60b0275f0bdcf1ac572bfd63ff7eaa61050ff54049168e9858279eec0'),
#                        bitcoin_signature_1=Sig('60', '4a77eec60b0275f0bdcf1ac572bfd63ff7eaa61050ff54049168e9858279eec0'),
#                        bitcoin_signature_2=Sig('50', '4a77eec60b0275f0bdcf1ac572bfd63ff7eaa61050ff54049168e9858279eec0'),
#                        features='',
#                        chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                        short_channel_id='115x1x0',
#                        node_id_1='02e493dbf1c10d80f3581e4904930b1404cc6c13900ee0758474fa94abe8c4cd13',
#                        node_id_2='02f9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f9',
#                        bitcoin_key_1='033f0e80e574456d8f8fa64e044b2eb72ea22eb53fe1efe3a443933aca7f8cb0e3',
#                        bitcoin_key_2='03e9623bbef1bf90ec0d7c744ed34659f010e6e638637161270ecd31e14f87f62e')

# CHAN_UPDATE_115x1x0_003 = Msg('channel_update',
#                               signature=Sig('03', 'd42e6feecf1cbb4428b026c7a3c76860531518d90ab9ea2aa94eee2fe1daec0a'),
#                               chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                               short_channel_id='115x1x0',
#                               timestamp=1565597764,
#                               message_flags=0,
#                               channel_flags=1,
#                               cltv_expiry_delta=144,
#                               htlc_minimum_msat=0,
#                               fee_base_msat=1000,
#                               fee_proportional_millionths=10)

# CHAN_UPDATE_115x1x0_004 = Msg('channel_update',
#                               signature=Sig('04', '03d22228832ced80b0f4985ecfea1da3d398cabb213159a66f8eccda312ea58c'),
#                               chain_hash='06226e46111a0b59caaf126043eb5bbf28c34f3a5e332a1fc7b2b73cf188910f',
#                               short_channel_id='115x1x0',
#                               timestamp=1565597765,
#                               message_flags=1,
#                               channel_flags=0,
#                               cltv_expiry_delta=48,
#                               htlc_minimum_msat=0,
#                               fee_base_msat=100,
#                               fee_proportional_millionths=11,
#                               htlc_maximum_msat=100000)
