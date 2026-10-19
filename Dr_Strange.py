import cv2
import mediapipe as mp
import math
import time
import os
import sys
import random
from pynput.mouse import Controller, Button

# =============================================================
# GRAPHICAL CYBER HUD BANNER SYSTEM
# =============================================================
def print_animated_banner():
    # ANSI Terminal Escape Color Codes
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    alias = "UNCL3_N3RD"

    # Pre-render hardware identification handshakes
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{CYAN}[+] CORE HARDWARE COMPONENT DETECTED: Mesa Intel(R) HD Graphics 520{RESET}")
    print(f"{CYAN}[+] SUBSYSTEM LINK STATUS...........: EGL INITIALIZED SUCCESS [OK]{RESET}\n")
    time.sleep(0.1)

    # -------------------------------------------------------------
    # DYNAMIC GRAPHIC HUD OVERLAY SCROLLER
    # -------------------------------------------------------------
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 100

    strange_title = "D R   S T R A N G E"
    strange_art = [
        "╔══════════════════════════════════════════════════════════════════════════════╗",
        "║                                                                              ║",
        "║                    ✦  D R   S T R A N G E  ✦                              ║",
        "║                                                                              ║",
        "╚══════════════════════════════════════════════════════════════════════════════╝"
    ]

    # Dynamic FREAKS OF THE SOCIETY message
    slogan = "⚡ 👁️  F R E A K S   O F   T H E   S O C I E T Y  👁️ ⚡"
    glitch_pool = ["X", "#", "%", "&", "█", "§", "@", "?", "*", "!"]

    # Animate DR STRANGE sliding into view
    max_shift = max(0, terminal_width - 76)
    for shift in range(0, max_shift + 1, 2):
        output_buffer = "\033[H"
        output_buffer += f"{MAGENTA}{BOLD}╔{'═' * max(20, min(74, terminal_width - 2))}╗{RESET}\n"

        for art_line in strange_art:
            output_buffer += " " * shift + f"{CYAN}{BOLD}{art_line}{RESET}\n"

        output_buffer += f"{MAGENTA}{BOLD}╚{'═' * max(20, min(74, terminal_width - 2))}╝{RESET}\n"
        output_buffer += f"\n{GREEN}{BOLD}        >>> {YELLOW}🌀  INVERSION MECHANICS  •  GESTURE ENGINE  •  🖐️{GREEN} <<<{RESET}\n"

        sys.stdout.write(output_buffer)
        sys.stdout.flush()
        time.sleep(0.025)

    # -------------------------------------------------------------
    # FREAKS OF THE SOCIETY — LARGE DYNAMIC TERMINAL SWEEP
    # -------------------------------------------------------------
    os.system('cls' if os.name == 'nt' else 'clear')

    slogan_width = len(slogan)
    sweep_space = max(4, terminal_width - slogan_width - 4)

    for shift in range(0, sweep_space + 1, 2):
        output_buffer = "\033[H"
        output_buffer += f"{CYAN}[+] SUBSYSTEM MATRIX LOADED INTO INVERSION ARCHITECTURE.{RESET}\n\n"

        # Graphical upper rail
        output_buffer += f"{MAGENTA}╔{'═' * max(30, min(78, terminal_width - 2))}╗{RESET}\n"

        # Dynamic moving slogan
        moving_slogan = ""
        for char in slogan:
            if char not in " ⚡👁️" and random.random() < 0.035:
                moving_slogan += f"{RED}{random.choice(glitch_pool)}{RESET}"
            else:
                moving_slogan += f"{GREEN}{BOLD}{char}{RESET}"

        output_buffer += " " * shift + f"{moving_slogan}\n"
        output_buffer += f"{MAGENTA}╚{'═' * max(30, min(78, terminal_width - 2))}╝{RESET}\n"

        sys.stdout.write(output_buffer)
        sys.stdout.flush()
        time.sleep(0.035)

    # Final static terminal greeting
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{CYAN}[+] SUBSYSTEM MATRIX LOADED INTO INVERSION ARCHITECTURE.{RESET}\n")

    print()
    print(f"{MAGENTA}{BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{MAGENTA}{BOLD}║                                                                              ║{RESET}")
    print(f"{CYAN}{BOLD}║                    ✦  D R   S T R A N G E  ✦                              ║{RESET}")
    print(f"{MAGENTA}{BOLD}║                                                                              ║{RESET}")
    print(f"{MAGENTA}{BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")

    print(f"\n{GREEN}{BOLD}       🌀  ⚡  {YELLOW}F R E A K S   O F   T H E   S O C I E T Y{GREEN}  ⚡  🌀{RESET}")
    print(f"{CYAN}              🖐️  GESTURE CONTROL  •  INVERSION ENGINE  •  👁️{RESET}\n")

    print(f"    {BOLD}{CYAN}>> IDENTITY ATTAINED:{RESET} {GREEN}⚡ {alias} ⚡{RESET}")
    print(f"    {BOLD}{CYAN}>> STATUS CLASSIFICATION:{RESET} {RED}⚙️  [ FREAKS OF THE SOCIETY CALIBRATED ] ⚙️{RESET}\n")
    time.sleep(0.2)

    # Technical boot validation logs
    boot_sequences = [
        "Connecting kernel interfaces to virtual gesture pipelines...",
        "Calibrating linear smoothing exponential filter interpolation matrices...",
        "Deploying structural MediaPipe hand landmark tracking engine mesh..."
    ]

    for seq in boot_sequences:
        time.sleep(0.15)
        print(f"    {GREEN}[⚡ LOAD]{RESET} {seq}")

    print(f"\n    {BOLD}{YELLOW}[!] SYSTEM FULLY DEPLOYED. CAMERA FRAME BUFFER IS LIVE.{RESET}\n")
    time.sleep(0.4)

# Trigger the terminal greeting sequences before framework compilation
print_animated_banner()

# Initialize Mouse and Camera Controllers
mouse = Controller()
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# MediaPipe processing pipelines
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils        
mp_drawing_styles = mp.solutions.drawing_styles  

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# -----------------------
# CONFIG
# -----------------------
SCREEN_W, SCREEN_H = 1920, 1080
SMOOTHING = 0.25      
DEADZONE = 0.04       
SCROLL_GAIN = 40      
HOLD_THRESHOLD = 0.8  

ALIAS_NAME = "UNCL3_N3RD"
BANNER_TEXT = "FREAKS OF THE SOCIETY"

# -----------------------
# STATE
# -----------------------
smooth_x, smooth_y = 0, 0
dragging = False

last_click_time = 0
CLICK_COOLDOWN = 0.35  

scroll_anchor_y = None
scroll_start_time = None

zoom_baseline_dist = None
start_time = time.time()

# -----------------------
# HELPERS
# -----------------------
def dist(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

def is_pinching(lm, finger_tip_idx):
    return dist(lm[4], lm[finger_tip_idx]) < 0.045

# -----------------------
# MAIN LOOP
# -----------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    left_hand = None
    right_hand = None

    if result.multi_hand_landmarks:
        for i, handLms in enumerate(result.multi_hand_landmarks):
            label = result.multi_handedness[i].classification[0].label

            if label == "Left":
                left_hand = handLms.landmark
            elif label == "Right":
                right_hand = handLms.landmark

            # Render overlay skeletal configurations onto screen frame
            mp_drawing.draw_landmarks(
                frame,
                handLms,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

    current_time = time.time()
    elapsed = current_time - start_time

    # =============================================================
    # RENDERING THE SMOOTH ANIMATED WINDOW HUD BANNER
    # =============================================================
    overlay = frame.copy()
    cv2.rectangle(overlay, (15, 15), (330, 85), (20, 20, 20), -1) 
    cv2.addWeighted(overlay, 0.75, frame, 0.25, 0, frame)

    pulse = int((math.sin(elapsed * 3) + 1) * 3) 
    cv2.rectangle(frame, (15, 15), (330, 85), (0, 140 + (pulse * 15), 255), 2) 

    slide_offset = int(max(0, 30 - (elapsed * 50))) 
    cv2.putText(frame, f"// SYS ACTIVE: {ALIAS_NAME}", (30 - slide_offset, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    breath_scale = 0.45 + (math.sin(elapsed * 2) * 0.02) 
    cv2.putText(frame, BANNER_TEXT, (30, 68), 
                cv2.FONT_HERSHEY_SIMPLEX, breath_scale, (0, 255, 180), 2, cv2.LINE_AA)

    # =============================================================
    # GESTURE SYSTEM INTERFACE PIPELINES
    # =============================================================
    if left_hand and right_hand:
        scroll_anchor_y = None
        scroll_start_time = None
        if dragging:
            mouse.release(Button.left)
            dragging = False

        # Fixed: Read index finger tip points (landmark index 8) for distance calculations
        d = dist(left_hand[8], right_hand[8])
        if zoom_baseline_dist is None:
            zoom_baseline_dist = d
        else:
            change = d - zoom_baseline_dist
            if abs(change) > 0.02:
                zoom_step = int(change * 150)
                if zoom_step != 0:
                    mouse.scroll(0, zoom_step)
                    zoom_baseline_dist += change * 0.2

    else:
        zoom_baseline_dist = None

        if right_hand:
            # Fixed: Read specific index tip positions (index 8) to bypass data array container errors
            x, y = right_hand[8].x, right_hand[8].y
            target_x = int(x * SCREEN_W)
            target_y = int(y * SCREEN_H)

            smooth_x = int(SMOOTHING * target_x + (1 - SMOOTHING) * smooth_x)
            smooth_y = int(SMOOTHING * target_y + (1 - SMOOTHING) * smooth_y)
            mouse.position = (smooth_x, smooth_y)

            # CLICK (Thumb + Index Pinch)
            if is_pinching(right_hand, 8):
                if current_time - last_click_time > CLICK_COOLDOWN:
                    mouse.click(Button.left, 1)
                    last_click_time = current_time

            # SELECT / DRAG (Thumb + Middle Finger Pinch)
            elif is_pinching(right_hand, 12):
                if not dragging:
                    mouse.press(Button.left)
                    dragging = True
            else:
                if dragging:
                    mouse.release(Button.left)
                    dragging = False
        else:
            if dragging:
                mouse.release(Button.left)
                dragging = False

        # ---------------------------------------------------------
        # LEFT HAND → SCROLLING WITH RELATIVE ANCHOR PROXIMITY
        # ---------------------------------------------------------
        if left_hand:
            # Fixed: Target the index tip (index 8) for scrolling calculations
            current_y = left_hand[8].y
            if scroll_anchor_y is None:
                scroll_anchor_y = current_y
                scroll_start_time = current_time
            else:
                delta_y = current_y - scroll_anchor_y
                if abs(delta_y) > DEADZONE:
                    hold_duration = current_time - scroll_start_time
                    speed_multiplier = SCROLL_GAIN * 3.5 if hold_duration > HOLD_THRESHOLD else SCROLL_GAIN
                    scroll_amount = int(delta_y * speed_multiplier)
                    if scroll_amount != 0:
                        mouse.scroll(0, -scroll_amount)
                else:
                    scroll_start_time = current_time
        else:
            scroll_anchor_y = None
            scroll_start_time = None

    # Render Display window frame
    cv2.imshow("Optimized Engine", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
