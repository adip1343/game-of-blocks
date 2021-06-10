# Metacoin
Metacoin is simple smart contract having functionality of sending tokens to each other. In this assignment we add loan functionality on top of it. Also we need to do various workarounds to do floating-point arithmatic with integers and avoiding overflow errors.

## Running the Code
1. Upload the file to Remix IDE and compile it.
2. Then we can deploy MetaCoin and Loan contracts for Owner 
3. Then we can play around with the functions provided to make sure they work properly.

## SafeMath Implementation
To prevent integer overflow errors we need to 

1. `add(a, b)` : returns `a+b` if doesn't overflow else throws error

2. `fullMul(a, b)` : returns `a*b` as `(h, l)` pair of integers.

3. `mulDiv(x, y, z)` : returns `x*y/z` if it doesn't overflow.

## Loan Implementation

1. `modifier isOwner()` :
    checker if modifier is `Owner` of `loan` contract

2. `function getCompoundInterest(uint256 principle, uint rate, uint time)` :
    calculates compound interest for given parameters

3.  `function reqLoan(uint256 principle, uint rate, uint time)`:
    request loan of calculated amount for `msg.sender`.  Value of this address is incremented in `loan` map.

4.  `function getOwnerBalance()`:
    returns balance of owner of Loan Contract.

5.  `function viewDues(address creditor)`:
    returns dues of `creditor`
    Only owner of Loan contract can call this function.

6.  `function settleDues(address creditor)`:
    if possible for owner settles dues with `creditor`.
    Only owner of Loan contract can call this function.