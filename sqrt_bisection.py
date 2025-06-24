def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square target must be non-negative.')
    
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
        return root
    
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
        return root
    
    else:
        low = 0
        high = max(square_target, 1)
        root = None

        # Start the bisection method loop, with a maximum number of iterations🔥
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid ** 2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid < square_target:
                low = mid
            else:
                high = mid
        
        if root is None:
            print(f'Failed to converge within {max_iterations} iterations.')
        else:
            print(f'The square root of {square_target} is approximately {root}')
        
        return root


N = float(input('Enter a number: '))
square_root_bisection(N)
