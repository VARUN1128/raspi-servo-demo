# 🤖 raspi-servo-demo

A Raspberry Pi–based demo for controlling a servo motor using Python and GPIO. This project is ideal for robotics, automation experiments, camera movement control, and DIY electronics learning.

---

## 🛠️ Project Overview

This project allows your Raspberry Pi to:
- Control a servo motor via GPIO
- Move to precise angles (0° to 180°)
- Sweep between angles smoothly
- Accept user input for repeat or quit
- Demonstrate real-time movement with printed logs

Perfect for beginner Raspberry Pi projects, robotics kits, and motor control learning.

---

## 🧰 Requirements

- Raspberry Pi (any model with GPIO)
- Micro servo motor (e.g., SG90)
- 3-pin servo wiring:
  - Signal → GPIO18 (Pin 12)
  - Power → 5V (Pin 2 or 4)
  - Ground → GND (Pin 6)
- Python 3
- RPi.GPIO library

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/raspi-servo-demo.git
cd raspi-servo-demo
````

2. **Install RPi.GPIO (if not installed)**

```bash
sudo apt update
sudo apt install python3-rpi.gpio
```

3. **Run the script**

```bash
python3 servo_demo.py
```

---

## 📄 Code Highlights

* Uses `RPi.GPIO` and `PWM` at 50Hz for servo control
* `set_angle(angle)` function converts degrees to duty cycle
* Includes auto-sweeping from 0° → 180° and back
* Interactive loop with `Enter` to repeat or `'q'` to quit

---

## 🔒 Safety Tips

* Use external power for multiple servos to avoid overloading the Pi
* Always call `GPIO.cleanup()` to release pins after execution
* Don't exceed servo angle limits (0–180°)

---

## 📸 Demo Output

```
Moving to 0 degrees
Moving to 90 degrees
Moving to 180 degrees
Sweeping from 0 to 180 degrees
Current angle: 0 degrees
...
Sweeping from 180 to 0 degrees
...
Press Enter to continue or type 'q' to quit:
```

---

## 📚 Learning Outcomes

* Basic PWM control with Raspberry Pi
* Servo angle calibration
* GPIO setup and cleanup
* Real-time feedback from hardware

---

## 🧠 Author

**Varun Haridas**
📧 [varun.haridas321@gmail.com](mailto:varun.haridas321@gmail.com)
🚀 Raspberry Pi & AI Enthusiast

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Contributions

Pull requests are welcome! Got an idea? Want to extend this with web control, joystick, or computer vision? Fork and build!

---

```

Would you like a `servo_demo.py` file attached or an HTML interface for controlling this via browser as the next step?
```
