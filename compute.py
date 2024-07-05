# Seunghoon Lee 
# seunghoon.lee.010@gmail.com

import sys

MAX_INPUT_NUM = 100

def compute(threshold, limit, nums):
    """
    Given a threshold and a limit, output numbers that are bigger than the threshold. However, total sum of those numbers must be smaller than the limit.

    Parameters:
        threshold (float/int): Threshold than which num in <nums> must be bigger.
        limit (float/int): Limit than which total of num in <nums> that are bigger than <threshold> must be smaller.
        nums ([float/int]): input numbers.

    Returns:
        [float]: differences between num in <nums> and threshold, and the total.
    """
    total = 0
    ans = []
    for num in nums:
        """
        if <num> (an input line) is greater than <threshold>, <output> is <num> - <threshold>.
        But we need to check if adding <output> to <total> will make it greater than <limit>.

        if <num> is smaller than <threshold>, <output> will be 0.0.

        If <room> (meaning room we have left before <total> reaches <limit>) is smaller than <output>, 
            we set <output> to <room>, since we need to ensure maximum output values.
        Otherwise,
            we set <output> to <num> - <threshold> since we have enough room left.
        """
        output = 0.0
        if num > threshold:
            output = num - threshold
            room = limit-total
            output = min(output, room)
            total += output
        
        ans.append(output)

    ans.append(float(total))
    return ans


if __name__ == '__main__':
    
    # Wrapping the entire block in a try catch block to handle uninteded user errors.
    # e.g. input is not convertible to float, is empty, etc.
    try:
        args = sys.argv

        if len(args) < 3:
            print("You need to provide at least two arguments in your command: python <filename> <limit> <threshold>. Every argument after will be ignored.")
            sys.exit()

        threshold = float(args[1])
        limit = float(args[2])

        # input intake. 100 is the maximum number of inputs. If the user enters an empty line (hits enter without writing anything), 
        # the program will compute an output with the arguments provided up until that point.
        nums = []
        for line in sys.stdin:
            nums.append(float(line))    

        ans = compute(threshold, limit, nums)

        for line in ans:
            print(line)

    except Exception as e:
        print(e)
        print("You need to provide at least two arguments in your command: python <filename: str> <limit: float> <threshold: float>. Every argument after will be ignored.")
        print("Every argument you input after must be convertible to float.")
    finally:
        sys.exit()

