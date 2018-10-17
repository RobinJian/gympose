class Human:
    def __init__(self, keypoints):
        #{0,  "Nose"},
        self.Nose = keypoints[0][0]
        #{1,  "Neck"},
        self.Neck = keypoints[0][1]
        #{2,  "RShoulder"},!!
        self.RS = keypoints[0][2]
        #{3,  "RElbow"},
        self.RE = keypoints[0][3]
        #{4,  "RWrist"},
        self.RW = keypoints[0][4]
        #{5,  "LShoulder"},!!
        self.LS = keypoints[0][5]
        #{6,  "LElbow"},
        self.LE = keypoints[0][6]
        #{7,  "LWrist"},
        self.LW = keypoints[0][7]
        #{8,  "MidHip"},
        self.MH = keypoints[0][8]
        #{9,  "RHip"},
        self.RH = keypoints[0][9]
        #{10, "RKnee"},
        self.RK = keypoints[0][10]
        #{11, "RAnkle"},!!
        self.RA = keypoints[0][11]
        #{12, "LHip"},
        self.LH = keypoints[0][12]
        #{13, "LKnee"},
        self.LK = keypoints[0][13]
        #{14, "LAnkle"},!!
        self.LA = keypoints[0][14]

        

    def test(self):
        return self.LS;
		
		
	def hwidth_fwidth(self):
		hwidth = abs(self.RW[0]-self.LW[0]);
		fwidth = abs(self.RA[0]-self.LA[0]);
		if hwidth > fwidth:
			return 1;
		else:
			return 0;
			
	def parallel(self):
		
			#陣列(肩膀)
		c1=self.RS;
		c2=self.LS;
			#存放兩個陣列的變數
		ans = list(map(lambda x: (x[0]-x[1]), zip(c2,c1)))
			#進行陣列內第0跟1位置的計算
		results= float(ans[1])/float(ans[0])
			#得出肩膀之斜率
		print(results)
			#印出肩膀結果
 
			#陣列(雙腳)
		d1=self.RA
		d2=self.LA
			#存放兩個陣列的變數
		ans2 = list(map(lambda x: (x[0]-x[1]), zip(d2,d1)))
			#進行陣列內第0跟1位置的計算
		results2= float(ans2[1])/float(ans2[0])
			#得出雙腳之斜率
		print(results2)
			#印出雙腳結果
		if abs(results-results2)<0.2:
			return 1
		else :
			return 0

# array1=[75,61,54]    
# array2=[42,10,21] 
#     #陣列(肩膀)
# c1=[array1[0],array1[1]]
# c2=[array2[0],array2[1]]
#     #存放兩個陣列的變數(第1.2位)
# ans = list(map(lambda x: (x[0]-x[1]), zip(c2,c1)))
#     #進行陣列內第0跟1位置的計算
# results= float(ans[1])/float(ans[0])
#     #得出肩膀之斜率

#     #印出肩膀結果
# array3=[167,85,12]    
# array4=[96,80,2] 
#     #陣列(雙腳)
# d1=[array3[0],array3[1]]
# d2=[array4[0],array4[1]]
#     #存放兩個陣列的變數
# ans2 = list(map(lambda x: (x[0]-x[1]), zip(d2,d1)))
#     #進行陣列內第0跟1位置的計算
# results2= float(ans2[1])/float(ans2[0])
#     #得出雙腳之斜率
# print(results2)
#     #印出雙腳結果
    
# if abs(results-results2)<0.2:
#     print(1)
# else :
#     print(0)
#     #計算兩者斜率是否差距超過0.2


