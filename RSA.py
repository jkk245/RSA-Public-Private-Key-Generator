'''
RSA Python Implementation
December 18/2016
JY
'''

import random;
import math;
import itertools;


#Large Distinct Primes (generated in wolfram alpha between 10^50 - 10^100) if my computer could actually run it 
#p = 5683017266155740037889935873782824214591294835090189767145048284399494690136075452819355543442045649;
#q = 2788106481246339386653402776686338906388220075784335732602151039593292618440640480492323924201819371;

p = 17;
q = 71;



#RSA Setup
n = p*q;
phi_n = (p-1)*(q-1);



#gcd uses the EEA
def gcd(a,b):
   while b != 0:
       a,b = b, a%b;
   return a;


#Public Key Creation
def choose_e(phi_n):
    e = random.randint(1, phi_n);
    
    while gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n);

    return e;



#Private Key Creation
#solve e*d cong 1 mod phi_n
#        d cong einverse mod phi_n
#        d = e^-1 % phi_n
#        find e^-1
#        e^-1 is e*x = 1 mod phi_n
#        d = e^-1 % phi_n

def choose_d(e, phi_n):
   
   #local defintion
   def invModulus(e,phi_n):
         
      for i in itertools.count(1,phi_n):
         r = (i * e) % phi_n;
         if r == 1:
            return i;       
   
      else:
         raise ValueError("%d has no inverse mod %d" % (e, phi_n));

   #return d
   d = invModulus(e,phi_n);
   return d;




def main():
   e = choose_e(phi_n);
   d = choose_d(e, phi_n);
   
   print ("The public key is (" + str(e) + "," + str(n) + ")");
   print ("The private key is (" + str(d) + "," + str(n) + ")");
   
   

main()

      

        

    
