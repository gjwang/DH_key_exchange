'''
Created on Mar 8, 2016

@author: gjwang
'''

class DHExchanger(object):
    '''
    DHExchanger
    Reference:
    https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
    https://github.com/gjwang/DH_ExchangeKey/blob/master/DH_ExchangeKey/main.cpp
    '''

    def __init__(self, g=5, p=23):
        '''
        Constructor
        '''
        self.g = g
        self.p = p
 
    def gernerate_public_key(self, key):
        return pow(self.g, key) % self.p

    def generate_share_key(self, public_key, private_key):
        return pow(public_key, private_key) % self.p

if __name__ == '__main__':
    exchanger = DHExchanger()
    a_private_key = 6
    a_publice_key = exchanger.gernerate_public_key(a_private_key)
    
    b_private_key = 15
    b_publice_key = exchanger.gernerate_public_key(b_private_key)
    
    a_share_key = exchanger.generate_share_key(b_publice_key, a_private_key)
    b_share_key = exchanger.generate_share_key(a_publice_key, b_private_key)
    
    print 'shareA=%s, shareB=%s'%(a_share_key, a_share_key)
    assert a_share_key == a_share_key

    for alice_priv_key in range(0, 16, 1):
        alice_pub_key = exchanger.gernerate_public_key(alice_priv_key)
        for bob_priv_key in range(0, 16, 1):
            bob_pub_key = exchanger.gernerate_public_key(bob_priv_key)

            alice_share_key = exchanger.generate_share_key(bob_pub_key, alice_priv_key)
            bob_share_key = exchanger.generate_share_key(alice_pub_key, bob_priv_key)
    
            print 'alice_priv_key=%s, bob_priv_key=%s'%(alice_priv_key, bob_priv_key)
            print 'alice_share_key=%s, bob_share_key=%s'%(alice_share_key, bob_share_key)
            assert alice_share_key == bob_share_key
            
