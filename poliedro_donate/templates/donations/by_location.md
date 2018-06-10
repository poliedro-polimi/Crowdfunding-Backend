---
tags: PoliMi Pride, PoliEdro
---

# {{ location.capitalize() }} campus pick-ups

{% for d in donations %}- [ ] **{{ d.pretty_id }}** - sg {{ d.stretch_goal }}, {{ d.items }} items - {{ d.reference.lastname }} {{ d.reference.firstname }}{% if d.notes %}
    - *Notes:* {{ d.notes }}{% endif %}
{% endfor %}