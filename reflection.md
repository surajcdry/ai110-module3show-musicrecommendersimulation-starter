# Reflection

## Profile Comparison Notes

### High-Energy Pop Fan vs. Chill Lofi Listener

The pop fan and the lofi listener live at opposite ends of the energy spectrum (0.85 vs. 0.35), and their top results reflect that completely. The pop fan gets fast, bright tracks; the lofi listener gets slow, quiet ones. What changed: every numerical feature (energy proximity score) flipped direction, and the genre filter pulled out entirely different pockets of the catalog. This makes sense — the two profiles were designed to be as different as possible, and the scoring treated them that way.

### Chill Lofi Listener vs. Deep Intense Rock Fan

These two share nothing in common. The lofi listener favors passive, background music; the rock fan wants something aggressive. The rock fan's top result (Storm Runner, energy=0.91) would score near the bottom of the lofi listener's list because its energy gap is enormous (+0.56 away from target). The output difference is stark: lofi top 5 are all under 0.5 energy, rock top 5 are all above 0.75. This validates that the energy scoring is doing real work and not just rubber-stamping genre matches.

### High-Energy Pop Fan vs. Deep Intense Rock Fan

These two are the most interesting comparison because they share the same energy range (~0.85–0.92) and both want "intense or happy, fast music." Yet their top results diverge because genre locks them into different tracks. Gym Hero appeared #2 for the rock fan despite being a pop song — because with only one rock song in the catalog, the system had to look outside the genre. This is actually a good sign: when genre matches are exhausted, energy and mood keep the list reasonable rather than returning random results.

## Overall Takeaway

The system is consistent and predictable, which is a strength and a weakness. Predictable means transparent and debuggable. But it also means a user who has wide taste will always see the same genre-first bubble. Real music discovery requires some randomness or diversity enforcement that this system doesn't have.
