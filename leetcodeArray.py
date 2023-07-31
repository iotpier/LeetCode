class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2) #bu rası sıralamak için sorted metodu şu işe yarar nums1 ve nums2 yi birleştirip sıralar
        if len(nums) % 2 == 0: #gelen sayıların uzunluğu çift ise
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2 #gelen sayıların uzunluğunun yarısını alıp ortalamasını alıyoruz
        else:
            return nums[len(nums)//2] #tek ise ortadaki sayıyı alıyoruz
        
        
        
from typing import List
# Path: leetcodeArray.py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        freq_dict = {} # burada boş bir sözlük oluşturuyoruz
        for num in nums: #nums içindeki numaraları döndürüyoruz
            freq_dict[num] = freq_dict.get(num, 0) + 1 #sözlüğe numaraları ekliyoruz ve sayılarını tutuyoruz 
                                                        #çünkü get metodu ile numaraları alıyoruz ve sayılarını tutuyoruz sonra 1 ekliyoruz

        # Adım 2  : Sözlüğü frekans değerine göre sıralayın
        sorted_elements = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)

        # Step 3: İlk k elemanı döndürün
        return sorted_elements[:k]

                
    
# Test commit 
        