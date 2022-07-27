from commands.commands import App


def main():
    try:
        app = App()
        app.setup()
        app.start()
    except Exception as e:
        print("Error starting the discord bot:", e)
    
if __name__ == "__main__":
    main()
