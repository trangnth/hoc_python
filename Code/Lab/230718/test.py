### Array

sequence_type_1 = ("one", "two", "three", "four", "five", "six", "seven")
sequence_type_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sequence_type_3 = "Hello Python"

# Phần tử đầu tiên
print(sequence_type_1[0]) # Hiển thị: one
# Phần tử thứ 2
print(sequence_type_1[1]) # Hiển thị: two
# Phần tử cuối cùng
print(sequence_type_1[6]) # Hiển thị: seven
print(sequence_type_1[-1]) # Hiển thị: seven

# In tu phan tu dau tien den phan tu 3
print(sequence_type_1[0:2])
print("Chieu dai cua chuoi: %d"%len(sequence_type_1)) # 7

# Lap qua tung phan tu, in nhung phan tu chia het cho 10
for num in sequence_type_2:
    print(num /10)
# Hien thi chi so index cua phan tu trong mang
for x, num in enumerate(sequence_type_1):
    print("Index: ", x, "Value: ", num)


