# Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder 1.0 suggests songs from a small catalog based on a user's preferred genre, mood, and energy level. It is designed for classroom exploration of how scoring-based recommender systems work. It is not intended for production use, real user accounts, or any commercial music service. Assume a single user with a fixed taste profile.

---

## 3. How the Model Works

For every song in the catalog, VibeFinder asks three questions:

1. **Does the genre match what the user likes?** If yes, the song earns 2 points.
2. **Does the mood match?** If yes, the song earns 1 point.
3. **How close is the song's energy to what the user wants?** A song whose energy is exactly right earns 1.5 points. The further the energy is from the target, the fewer points it gets, down to 0.

After scoring every song this way, the system sorts them from highest to lowest score and returns the top five. Each recommendation comes with a plain-English explanation of exactly which points it earned.

---

## 4. Data

- **Size:** 18 songs (10 from the starter kit, 8 added manually)
- **Features per song:** id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness
- **Genres represented:** pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, country, metal, classical, r&b, electronic, reggae, folk
- **Moods represented:** happy, chill, intense, moody, focused, relaxed, confident, sad, romantic, energetic, nostalgic
- **What's missing:** No listening history, no artist popularity signals, no lyrics or language features. The dataset skews toward English-language Western pop and rock because those are the most familiar genres to build examples around.

---

## 5. Strengths

- Works well for users with clear, consistent preferences (e.g., someone who always wants high-energy pop).
- Explanations are transparent — the user can see exactly why each song was recommended.
- Simple enough to reason about and debug by hand.
- The chill/lofi profile produced very intuitive results: both top picks were lofi/chill songs with matching low energy.
- The rock/intense profile correctly surfaced Storm Runner as the single obvious top match.

---

## 6. Limitations and Bias

- **Genre over-dominates.** Genre carries 2x the weight of mood. A pop/happy song will almost always beat a jazz/happy song even if the jazz song is a near-perfect energy match. This creates a genre bubble: once you declare a favorite genre, very few songs outside it will crack the top 5.

- **Small dataset amplifies bias.** 4 out of 18 songs are lofi, 3 are pop, and 1 each for metal, classical, country, folk, reggae, and r&b. Underrepresented genres produce fewer good matches, so users who prefer those genres get sparser results.

- **Energy is linear, not perceptual.** The formula treats the gap between 0.3 and 0.4 exactly like the gap between 0.7 and 0.8. In reality, both 0.7 and 0.8 feel "high energy," so this might unfairly penalize close matches.

- **No diversity enforcement.** The same artist (e.g., LoRoom) can occupy multiple top slots, making the list feel repetitive.

- **Profile is one-dimensional.** The system cannot handle "I want chill music unless I'm working out" or any context-dependent preferences.

---

## 7. Evaluation

Three user profiles were tested:

| Profile | Top Result | Matched Intuition? |
|---|---|---|
| High-Energy Pop Fan (genre=pop, mood=happy, energy=0.85) | Sunrise City | Yes — perfect triple match |
| Chill Lofi Listener (genre=lofi, mood=chill, energy=0.35) | Library Rain | Yes — lofi/chill/low energy |
| Deep Intense Rock Fan (genre=rock, mood=intense, energy=0.92) | Storm Runner | Yes — only rock song in catalog |

**Experiment — halving genre weight (2.0 → 1.0):**
The chill profile's top result shifted from lofi tracks to an ambient track, because ambient had a slightly closer energy match. Rankings became more "vibe-driven" and less "genre-locked," confirming that genre weight is the single most influential parameter.

**Surprise:** Gym Hero (pop/intense) ranked 2nd for the intense rock profile because its energy (0.93) was nearly identical to the target (0.92) and its mood matched. Genre was the only mismatch. This shows the system already partially escapes genre bubbles when energy and mood are strong enough.

---

## 8. Future Work

- **Add collaborative filtering:** Match users to other users with similar taste profiles, not just songs. This is how Spotify's "Discover Weekly" finds music outside your usual genres.
- **Add a diversity penalty:** If the top results have two songs from the same artist, reduce the second one's effective score to encourage variety.
- **Expand the dataset:** 18 songs is too small for meaningful recommendations outside the three or four dominant genres. 100+ songs would show the algorithm's real behavior.

---

## 9. Personal Reflection

The biggest surprise was how much the weights controlled the "personality" of the recommender. Changing genre from +2.0 to +1.0 felt like switching from a genre guide to a vibe guide — a completely different product, just from one number. That made me realize how many invisible editorial decisions are baked into real recommender systems like Spotify or YouTube, often without users knowing. When YouTube keeps showing you the same type of video, it might just be because someone set a content-category weight too high years ago.

Using AI tools for this project was most helpful at the design stage — asking for suggestions on feature weighting strategy saved me from trying every combination by hand. But I still had to verify the output made intuitive sense by running the profiles manually and reasoning about whether the results "felt right." The tools were fast at generating options; the judgment about which option was correct stayed with me.
