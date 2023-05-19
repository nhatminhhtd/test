import time
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_ST7735 as TFT
from PIL import Image, ImageDraw

# Cấu hình giao diện SPI
DC = 18
RST = 22
SPI_PORT = 0
SPI_DEVICE = 0
disp = TFT.ST7735(
    DC,
    rst=RST,
    spi=SPI.SpiDev(
        SPI_PORT,
        SPI_DEVICE,
        max_speed_hz=4000000
    ),
    width=128,
    height=160
)

# Khởi tạo màn hình
disp.begin()

# Tạo ảnh mới với màu nền
image = Image.new('RGB', (disp.width, disp.height), (0, 0, 0))
draw = ImageDraw.Draw(image)

# Vẽ một hình vuông đỏ ở giữa màn hình
draw.rectangle((30, 30, 100, 100), outline=(255, 0, 0), fill=(255, 0, 0))

# Hiển thị ảnh lên màn hình
disp.display(image)

# Dừng lại trong 5 giây
time.sleep(5)

# Xóa màn hình
disp.clear()

# Kết thúc chương trình
disp.cleanup()
