# [WRITEUP] WAITING FOR LOVE

[debai](https://i.imgur.com/rXK6u9w.png)

Mở chương trình trong Detect It Easy ta được:

!(https://i.imgur.com/i4OdLRN.png)

Ta có hàm main():

[MAIN](https://i.imgur.com/t5PFzEn.png)

Ta phân tích hàm **sub_401530()**

[hamdequy](https://i.imgur.com/udbMW34.png)

Hàm **sub_401530()** là hàm đệ quy với tham số giảm dần, kết thúc khi tham số bé hơn 3. Tuy nhiên, thanh ghi EAX là thanh ghi 32 bits, nên chỉ lưu được giá trị <= 4294967295. Đây là cách hoạt động thanh ghi 32bits:

[eax](https://i.imgur.com/bfhiWwt.png)

[Imgur](https://i.imgur.com/z8V3onA.png)

[Imgur](https://i.imgur.com/PxOlIiR.png)

Ta quan sát đặt khi này thanh ghi AL có giá trị là 0X4D tức là chứ 'M' sau khi qua hàm **sub_46ED70()** thanh ghi vẫn trở về **0** và in chữ **M**. Cứ như thế in ra chữ MSEC rồi bị lỗi tại hàm **sub_401530()**. Do hàm đệ quy thời gian thực hiện lớn nên với tham số lớn thì chương trình không thực hiện được. Do đó ta sử chương trình thành vòng lặp for:

[end](https://i.imgur.com/KV8lXe5.png)

Kết quả của hàm đệ quy sử dụng kết quả của tham số sau nên tôi đã lưu giá trị của kết quả cũ vào arr1[] , và tại arr1[n] chính là giá trị của hàm đệ quy nếu không lỗi. Lưu ý do giá trị được lưu vào thanh ghi **AL** nên ta *&0xff* để lấy 2 giá trị cuối.

Flag: MSEC{r3cuRs10n_1s_F4t4st1C_Hehe?}
