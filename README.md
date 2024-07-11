# Airchain-Error-Fixer
این اسکریپت برای نود ایرچین است اگر نودتون به ارور بخوره اتوماتیک سرویسش رو ریست میکنه تا نود ادامه مسیر رو بره و قطع نشه

##مراحل استفاده 
1. پایتون را نصب کنید
```
sudo apt install python3
```
2. فایل را دانلود کنید
    ```bash
    git clone https://github.com/xONEIROS/Airchain-Error-Fixer.git
    cd Airchain-Error-Fixer
    ```

3. یک اسکرین جدید بسازید
    ```bash
    screen -S log-monitor
    ```
4. کد را اجرا کنید
   ```bash
    sudo python3 monitor.py
    ```
    کلیدهای `Ctrl+A` را فشار داده و سپس `D` را بزنید تا از سشن جدا شوید و اسکریپت در پس‌زمینه اجرا شود.


### بازگشت به سشن Screen

اگر نیاز به بازگشت به سشن screen داشتید، از دستور زیر استفاده کنید:

```bash
screen -r log-monitor
