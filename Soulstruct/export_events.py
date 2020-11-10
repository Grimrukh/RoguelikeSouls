from soulstruct.events.darksouls1 import convert_events

if __name__ == '__main__':
    convert_events(
        ".emevd.dcx",
        "G:/Steam/steamapps/common/DARK SOULS REMASTERED/RoguelikeSouls/Package/event",
        # "G:/Steam/steamapps/common/DARK SOULS REMASTERED/event",
        ".evs.py",
        "events",
    )
