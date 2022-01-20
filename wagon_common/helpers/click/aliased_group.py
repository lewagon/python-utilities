# from https://click.palletsprojects.com/en/8.0.x/advanced/

import click


class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        commands = [cmd for cmd in self.list_commands(ctx) if cmd.startswith(cmd_name)]
        if not commands:
            return None
        elif len(commands) == 1:
            return click.Group.get_command(self, ctx, commands[0])
        ctx.fail(f"Too many commands match the alias: {', '.join(sorted(commands))}")

    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args
