# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	res = ""
	s = str2[:1:]
	for i in str1:
		if s == i:
			break
		res += i
	
	for i in range(len(str1)):
		if str1[i] == s:
			st = str1[i::]
	
	result = st + res
	if result == str2:
		return True
	else:
		return False

print(isrotated("XYZ", "ZXY"))
print(isrotated("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZA"))
print(isrotated("12345", "54321"))