'''
---------------------------
RSA Public Private Key Generator
December 18/2016
JY
---------------------------
'''

import random;
import math;
import timeit;

#Timer
start = timeit.default_timer();

#Large Distinct Primes (generated in wolfram alpha between 10^50 - 10^100) if my computer could actually run it that is
#p = 5683017266155740037889935873782824214591294835090189767145048284399494690136075452819355543442045649;
#q = 2788106481246339386653402776686338906388220075784335732602151039593292618440640480492323924201819371;

#Sample small primes
p = 983;
q = 157;


#---------------------
#RSA Setup
#---------------------

n = p * q;

#Euler's Totient Function
phi_n = (p - 1) * (q - 1);



#GCD calculation using the EEA
def gcd(a,b):
   while b != 0:
       a, b = b, a%b;
   return a;


#---------------------
#Public Key Creation
#---------------------
#Choose public value e as a random integer such that e and phi_n are coprime

def choose_e(phi_n):
    e = random.randint(1, phi_n);
    
    while gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n);

    return e;


#---------------------
#Private Key Creation
#---------------------
#Solve (e * d) congruent 1 mod phi_n for private key value d
#           d congruent einverse mod phi_n
#           d = e^-1 % phi_n
#
#To find e^-1:
#        e^-1 is (e * i) = 1 mod phi_n
#        d = (e * i) % phi_n such that when d = 1, x is the modular inverse of e

def choose_d(e, phi_n):
   
   #local defintion
   def invModulus(e,phi_n): 
      while True:
         for i in range(1, phi_n):
            r = (i * e) % phi_n;
            if r == 1:
               return i;
               exit
      
   d = invModulus(e, phi_n);
   return d;



def main():
   e = choose_e(phi_n);
   d = choose_d(e, phi_n);
   stop = timeit.default_timer();
   
   print ("The public key is (" + str(e) + "," + str(n) + ")");
   print ("The private key is (" + str(d) + "," + str(n) + ")");
   print (stop - start);
   
   

main()
