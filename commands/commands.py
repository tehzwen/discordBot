import interactions
import subprocess
from server.server import Server
from utils.secrets import loadSecrets


class App:
    def __init__(self) -> None:
        self.secrets = loadSecrets("secrets.json")
        self.bot = interactions.Client(token=self.secrets["DISCORD_CLIENT_TOKEN"])
        self.server_data = {}

        if "SERVERS" in self.secrets:
            for s in self.secrets["SERVERS"]:
                self.server_data[s['name']] = Server(s)

    def start(self):
        self.bot.start()

    def setup(self):
        @self.bot.command(
            name="hello",
            description="This is the first command I made!",
            scope=self.secrets['DISCORD_SERVER_ID'],
            options=[
                interactions.Option(
                    name="text",
                    description="What you want to say",
                    type=interactions.OptionType.STRING,
                    required=True,
                ),
            ],
        )
        async def hello_command(ctx: interactions.CommandContext, text: str):
            await ctx.send(text)

        @self.bot.command(
            name="ping",
            description="Pings the server named if it is found",
            scope=self.secrets['DISCORD_SERVER_ID'],
            options=[
                interactions.Option(
                    name="name",
                    description="Server name",
                    type=interactions.OptionType.STRING,
                    required=True,
                ),
            ],
        )
        async def ping_command(ctx: interactions.CommandContext, name: str):
            await ctx.send(f"Attempting to ping server: `{name}`")

            # look up the server by name
            if name in self.server_data:
                output = subprocess.getoutput(self.server_data[name].ping())
                await ctx.send(f"```{output}```")
                return

            await ctx.send(f"Server with name `{name}` not found")

        @self.bot.command(
            name="list_servers",
            description="Lists all possible servers to manage",
            scope=self.secrets['DISCORD_SERVER_ID']
        )
        async def list_servers(ctx: interactions.CommandContext):
            total_msg = ""

            for k in self.server_data:
                total_msg += f"`{k}`\n"

            total_msg += "\n"
            await ctx.send(total_msg)
