from soulstruct.darksouls1r.events import convert_events

if __name__ == '__main__':
    convert_events(
        ".emevd.dcx",
        "G:/Dark Souls/Projects/RoguelikeSouls/Package/event",
        # "G:/Steam/steamapps/common/DARK SOULS REMASTERED/event",
        ".evs.py",
        "events",
    )
