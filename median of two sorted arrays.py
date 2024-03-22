def findMedianSortedArrays(self,m,nums1,n,nums2):
    #merge the arrays into a single sorted array
    merged=nums1+nums2
    merged.sort()
    t=len(merged)
    if t%2==1:
        return(merged[t//2])
    else:
        mid1=merged[t//2-1]
        mid2=merged[t//2]
        return((mid1+mid2)/2)


m=int(input())
nums1=list(map(int, input().strip().split()))[:m]
n=int(input())
nums2=list(map(int, input().strip().split()))[:n]
a=findMedianSortedArrays(m,nums1,n,nums2)
print(a)

