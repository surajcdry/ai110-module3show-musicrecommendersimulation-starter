"""
Command line runner for the Music Recommender Simulation.

Run with:
    python -m src.main
"""

from src.recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print top-k recommendations for a user profile in a readable format."""
    recommendations = recommend_songs(user_prefs, songs, k=k)
    print(f"\n{'='*55}")
    print(f"  Profile: {profile_name}")
    print(f"  Prefs:   genre={user_prefs['genre']}, mood={user_prefs['mood']}, energy={user_prefs['energy']}")
    print(f"{'='*55}")
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  {i}. {song['title']} — {song['artist']}")
        print(f"     Score: {score:.2f}")
        print(f"     Why:   {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop Fan": {"genre": "pop", "mood": "happy", "energy": 0.85},
        "Chill Lofi Listener": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock Fan": {"genre": "rock", "mood": "intense", "energy": 0.92},
    }

    for name, prefs in profiles.items():
        print_recommendations(name, prefs, songs, k=5)


if __name__ == "__main__":
    main()
