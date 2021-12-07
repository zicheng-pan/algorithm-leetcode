class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0
        length = len(nums)
        ans = [0 for _ in range(length)]
        account = 0

        for i in range(len(ans)):
            if i <= max_index:
                for j in range(nums[i] + 1):
                    ans[i] = max( j + i, ans[i])
                max_index = max(max_index,ans[i])
                account = account + 1
                if max_index + 1 >= length:
                    return True
        return False






solution = Solution()
print(solution.canJump([3,2,1,0,4]))
# [2,3,1,1,4]
print(solution.canJump([0]))
print(solution.canJump([2,3,1,1,4]))
print(solution.canJump([3,0,8,2,0,0,1]))
print(solution.canJump([15258,19305,14766,1718,16691,96,10334,5991,16181,6013,18027,8737,8679,16840,385,11716,13922,8304,19002,2912,5142,2957,3378,708,14751,13474,14631,3539,12080,11656,3916,3052,7955,18822,14155,207,2085,12975,3719,6274,3545,18967,16698,4833,16653,18439,12271,3919,4264,3476,9761,5179,14912,5858,6911,9959,17162,9842,14146,8226,7250,4905,4131,13814,9388,798,3680,9642,9583,865,17039,4005,17158,4125,14156,966,8393,19548,5680,4971,1305,4011,19044,2867,16213,6842,4049,14823,10978,17841,14711,5876,4723,6190,10456,17445,7477,385,15734,4815,13856,12815,5775,15087,4923,8304,10896,18569,9274,11311,16329,16896,5767,13687,5721,2236,17790,9596,8192,19712,6097,4732,14968,8027,15798,2396,15807,14969,14180,8362,15910,19475,13674,8101,16424,5207,10926,2954,4973,11346,14434,657,11379,2220,3963,1822,11999,1754,14670,9390,1981,82,16657,12038,19645,8525,8794,7471,4150,6057,4520,6544,6163,17370,6417,14119,3139,5439,19070,12830,7441,8550,19621,17352,4992,6869,19083,17815,17934,721,11329,1467,7322,9903,10509,10752,2088,9527,17134,9919,9918,16875,16169,9714,12770,13733,19442,9935,6834,11174,17648,5535,1144,5914,6050,1568,12986,4715,4996,4073,13779,6961,3090,19745,11933,840,13712,7640,10436,2450,17950,17808,4509,12766,14637,17416,2715,9030,4506,11995,17899,7762,16481,13175,5422,14606,14073,1969,5701,994,2151,4966,3948,14478,12917,523,6993,6855,14310,13872,18700,19627,8408,431,6157,12100,17828,5498,4966,19208,12670,14756,15646,6317,13015,9815,19982,6582,14435,4873,4906,18427,7966,16436,5844,8540,4387,2497,6135,776,17649,11931,2555,13103,14437,3049,758,425,71,19470,13026,10457,17540,9600,10300,14227,5785,5973,17429,16592,9654,19585,10977,1703,10704,3487,14206,15971,15792,8015,9003,10584,6602,12930,1277,11104,16939,1267,2900,8086,18853,10395,10832,15401,7663,4150,130,7940,4749,7665,16036,379,9252,5854,17498,9151,18291,10018,18552,6525,4239,18044,1697,12789,10196,12663,6649,4481,12464,2341,5089,18312,17166,2210,15539,11780,5565,14840,6219,13736,856,16636,17050,9856,15421,5527,17043,13730,17043,18455,2796,3922,14597,3065,1454,13586,1728,4483,10069,13321,4063,2318,4076,7206,15751,16189,6533,4746,3325,19417,10746,4573,13475,5510,11723,7436,18464,2518,17086,9052,5170,4054,148,6762,17972,15367,15759,2256,1579,16502,18156,7564,12790,3104,19598,9596,14678,17794,3565,11258,7080,12487,15970,414,10725,8504,9634,3384,7727,10470,375,792,19801,17168,6854,17668,10215,13015,10351,19990,17801,5475,11348,7688,4661,366,8506,8101,19759,18292,17771,14268,12802,17325,15706,14396,6877,10970,2039,12148,7672,16960,6770,17070,6836,3713,2391,18226,15136,11442,5068,17664,14014,16969,2153,17283,6509,3357,5273,17031,16824,17445,9291,14772,8937,8708,3392,13107,3064,11995,2295,10503,16579,442,17730,14281,4003,732,17479,15239,2104,2123,6432,152,789,18640,9814,11379,18375,9731,19579,4756,18040,11878,3011,11444,11405,6667,1712,2856,17782,1492,11327,10782,10985,1044,2771,19105,14769,19550,17704,18470,15810,16352,4117,17812,3921,7161,2374,8951,16150,6903,6955,8961,16797,13168,17605,6047,8485,11598,19459,12990,4162,11639,10510,17382,17244,3985,5423,6522,19226,7339,13983,16574,4419,11188,17572,10678,520,8614,3080,112,9780,15854,4268,5403,11266,11435,7838,6883,11457,2816,4840,7340,300,19943,7658,9040,13251,5161,9937,14299,9020,10670,3944,1617,5046,16518,15549,17170,3123,2413,8052,888,4315,16229,7783,17486,7643,4282,18016,11936,9368,8738,10162,10540,15783,8403,5049,2174,10882,14933,1329,4885,19761,5677,16060,12041,18546,13384,3527,15620,1858,3679,10363,5369,13340,10568,2522,12850,12863,3818,3452,17849,5551,6824,16670,5514,16445,13704,2869,1016,633,16565,5555,915,17912,2114,4256,2791,13724,7366,5677,1859,12683,1387,7838,6394,14965,7882,5635,4889,1369,17687,8255,10207,13648,8179,19690,3529,11115,16345,11518,1833,12298,2062,7297,1522,5014,18001,1211,17767,9716]))