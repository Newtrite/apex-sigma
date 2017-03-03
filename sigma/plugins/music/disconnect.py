import discord


async def disconnect(cmd, message, args):
    if not message.author.voice_channel:
        embed = discord.Embed(
            title=':warning: I don\'t see you in a voice channel', color=0xFF9900)
        await cmd.bot.send_message(message.channel, None, embed=embed)
        return
    voice = cmd.bot.voice_client_in(message.server)
    cmd.music.queues[message.server.id] = None
    await voice.disconnect()
    embed = discord.Embed(color=0x66CC66, title=f':white_check_mark: Disconnected From {voice.channel.name}')
    embed.set_footer(text='And purged queue.')
    await cmd.bot.send_message(message.channel, None, embed=embed)
