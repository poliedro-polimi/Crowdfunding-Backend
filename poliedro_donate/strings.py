LANGS = ("it", "en")

PP_ITEM_NAME = {
    "it": "Donazione a favore di PoliEdro",
    "en": "Donation to PoliEdro"
}

_PP_ITEM_DESC = {
    "en": "With gadget reservation: {qty}x {item}",
    "it": "Con prenotazione gadget: {qty}x {item}"
}

_PP_ITEM_DESC_STRETCH_0 = {
    "en": "No gadgets requested, thanks for your support!",
    "it": "Nessun gadget richiesto, grazie del supporto!"
}

PP_ITEM_DESC = lambda lang, stretch_goal, qty: \
    _PP_ITEM_DESC_STRETCH_0[lang] if stretch_goal == 0 else \
        _PP_ITEM_DESC[lang].format(qty=qty, item=STRETCH_GOAL_NAMES[lang][stretch_goal])

STRETCH_GOAL_NAMES = {
    "it": {
        0: "(nessuno)",
        1: "Shopper PoliMi Pride",
        2: "Shopper, spillette e adesivi PoliMi Pride",
        3: "Kit completo PoliMi Pride - shopper, splillette, adesivi, maglietta/canotta"
    },

    "en": {
        0: "(none)",
        1: "PoliMi Pride shopper bag",
        2: "PoliMi Pride shopper bag, pins and stickers",
        3: "PoliMi Pride Full Kit - shopper bag, pins, stickers, t-shirt/tank top"
    }
}

PP_NOTE_TO_PAYER = {
    "it": "In caso di domande o ripensamenti, scrivi a info@poliedro-polimi.it",
    "en": "If you have a question or change your mind, send an email to info@poliedro-polimi.it"
}