# ***Login*** (100pts):

## Bài này giống như của Flare on 8 ( bài 1) nên tương đối dễ

> var form = document.getElementById("credform");
> var username = document.getElementById("usrname");
> var password = document.getElementById("psw");
> var info = document.getElementById("infolabel");
> var checkbtn = document.getElementById("checkbtn");
> var encoded_key = "GQsLLyJnURY1XycvEjkOahYRfRE="
> 
> function dataEntered() {
>     if (username.value.length > 0 && password.value.length > 0) {
>         checkbtn.disabled = false;
>     } else {
>         checkbtn.disabled = true;
>     }
> }
> 
> function checkCreds() {
>     if (username.value == "Admin" && atob(password.value) == "MsecN3WBI3") 
>     {
>         var key = atob(encoded_key);
>         var flag = "";
>         for (let i = 0; i < key.length; i++)
>         {
>             flag += String.fromCharCode(key.charCodeAt(i) ^ password.value.charCodeAt(i % password.value.length))
>         }
>         document.getElementById("banner").style.display = "none";
>         document.getElementById("formdiv").style.display = "none";
>         document.getElementById("message").style.display = "none";
>         document.getElementById("final_flag").innerText = flag;
>         document.getElementById("winner").style.display = "block";
>     }
>     else 
>     {
>         document.getElementById("message").style.display = "block";
>     }
> }

    Tại đây ta chú ý 2 hàm sau: **dataEntered()** và **checkCreds()**:

         1. Hàm **dataEnter** kiểm tra username và password có được nhập vào không.

         2. Hàm **checkCreds()**: 

                        username là **"Admin"** và password = **btoa(MsecN3WBI3)**. Hàm btoa() trong Javascript có  chức năng tương                         tự như  *base64 decode*. Phần dưới chủ yếu là in flag thui. Bác nào thích thì cứ giải :3. Chủ yếu là lấy từng ký                         tự của **password** XOR **atob(encode_key)** Ta mở [CyperChef]([CyberChef](https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')&input=TXNlY04zV0JJMw)) và dễ dàng có được:[Imgur](https://i.imgur.com/ycqAwlr.png)

        Nhập tất cả vào ta sẽ được kết quả như sau:[Imgur](https://i.imgur.com/GFX8uFX.png)


