# THE PYTHON SECTION OF THE BOT 
# my phton is still veryy limited and im just learning it 


#TOP CMD IS TO EXPLANE USE (its not super user friendly )

async def BLhelp(ctx, cmd):
    ts = time.time()
    user = bot.get_user
    import asyncio
    from pavlov import PavlovRCON
    pavlov = PavlovRCON(f"{SERVER_IP}", f"{SERVER_PORT}", f"{RCONPASS}")
    data = await pavlov.send(f"ban {steamid}")
    await ctx.send('!BL "7656119818507282.420.he told me my finger smells like cheese and mom says i cant have dairy"')

#THE ACTUAL BAN CMD WELL THE PYTHON PART
@bot.command ( pass_context = True ) 
@commands.has_role("Admins")
async def BL(ctx, banArg):
    
    ts = time.time()
    list = banArg.split(".")
    num = len(list)
    import asyncio
    userid = list[0]
    days = list[1]
    reason = list[2]
    global steamid
    steamid = int(list[0]) 
    print(len(userid))
    if len(userid) == 17 :  
        from pavlov import PavlovRCON
        pavlov = PavlovRCON(f"{SERVER_IP}", f"{SERVER_PORT}", f"{RCONPASS}")
        data = await pavlov.send(f"ban {steamid}")
        subprocess.run(f"bash /home/steam/code/tempbans/unBAN.sh {steamid} {days} ", shell=True, check=True)
        user = bot.get_user
        channel = bot.get_channel(1137790193064214640)
        if channel:
            await channel.send(f'  - - - - - BAN LOG EVENT {ct} \n admin `{ctx.message.author}` submited a ban for player `{steamid}` and the ban will be for `{days}` days** and the ban is for `{reason}`  \n - - - - - - - - - - - - - - ')
    else:
        await ctx.send(f'admin {ctx.message.author} submited a ban for player `{userid}` but the ban has FAILED')
        print(" ")

        
