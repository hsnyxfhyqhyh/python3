count = 0

# 著名的汉诺塔问题， 需要把一串按大小顺序的由上往下放在A 柱上的圆盘移到C 上， 移动过程中不能有小圆盘在大圆盘下方。 
# 问题拆解为n-1 个圆盘， 和最下方的大圆盘。 这个问题就变成了 
        # 而其余的n-1圆盘都串在B 柱上， 而要实现其他n-1的圆盘在B  柱上， 要用到拆解过程中的第一步骤。 
        # 第n个 圆盘由A 移动到C， 即是第二步骤。 
        # 接下来的步骤是把n-1的圆盘，从其实位置B, 移到终止位置 C, 可以经由 A 
        
def hanoi(n, src, dst, mid):
    global count    
    
    if n==1: 
        print("{}: {}->{}".format (1, src, dst))
        count +=1
    else :
        hanoi(n-1, src, mid, dst)                   # 第一步骤
        print("{}: {}->{}".format (n, src, dst))    # 第二步骤。 
        count += 1
        hanoi(n-1, mid, dst, src)                   # 第三步骤。 

hanoi(7, "A", "C", "B")
print (count)