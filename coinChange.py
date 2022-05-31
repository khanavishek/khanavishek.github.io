'''
The Coin Change Problem: 

322. Coin Change (Leetcode)

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


'''


#Sub-problems


#DP[0] = minimum number of coins to make 0 cents
#DP[n] = minimum number of coins to make n cents 


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    #Create a DP_table for i to n, where n is the the amount, so building the tree
    #bottom up 
    
    
    '''
    
    DP= [inf,inf, inf,inf] initialize everything with something that's impossible

    '''
    '''
    Define sub-problems = DP_table[i] = minimum number of coins to make i-cents 
    DP_table[0.....n]
    len(DP_table) == n+1
    
    '''
    
    DP_table = []
    for i in range(amount+1):
        DP_table.append(amount+1)
        
    DP_table[0] = 0 

    
    coins = sorted(coins)
    
    #Now we begin filling the DP_table
    for i in range(amount+1):
        #we need to see if grabbing that coin is going to to lead to a solution
        #sort of like a DFS (????)
        for coin in coins: 
            
            #This is the transition function
            
            #check if adding that coin gets you to the amount
                if coin <= i: 
                    DP_table[i] = min((DP_table[i-coin] +1), DP_table[i])
            
        
    if DP_table[amount] < (amount+1):
        return DP_table[amount]
    else:
        return -1


print(coinChange([1,2,5],11))

'''
index :    0	1	2	3	4	5	6	7	8	9	10	11
DP_table = [0	1	1	2	2	1	2	2	3	3	2	3]
'''


print(coinChange([2],3))
    
'''

index:   0	1	2	3
DPtable: 0	4	1	4

'''
