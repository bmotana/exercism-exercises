def triplets_with_sum(number: int) -> list[list[int]]:
    """Find Pythagorean triplets where a + b + c = number.
    
    Args:
        number: The target sum for the triplets
        
    Returns:
        A list of lists containing the Pythagorean triplets that sum to number
    """
    triplet_list = []
    
    # Find all primitive Pythagorean triplets that could be scaled to sum to number
    # Then check which scales work
    m_max = int((number // 2) ** 0.5) + 1
    
    for m in range(2, m_max):
        for n in range(1, m):
            # Ensure m and n have opposite parity and are coprime
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                # Generate primitive triplet
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                
                # Sum of the primitive triplet
                prim_sum = a + b + c
                
                # Check if this can be scaled to match our target
                if number % prim_sum == 0:
                    # Scale factor
                    k = number // prim_sum
                    
                    # Scale the triplet
                    triplet = sorted([k*a, k*b, k*c])
                    triplet_list.append(triplet)
    
    # Also consider primitive triplets without the coprime constraint
    for m in range(2, m_max):
        for n in range(1, m):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            
            triplet_sum = a + b + c
            
            # Check if this triplet sums to our target
            if triplet_sum == number:
                triplet = sorted([a, b, c])
                if triplet not in triplet_list:
                    triplet_list.append(triplet)
    
    return triplet_list

def gcd(a, b):
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a