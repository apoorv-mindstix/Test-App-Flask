from dataclasses import dataclass, field

@dataclass
class UserRepoModel:
    user_id: int
    email: str
    role: str
    # roleSpecificId: int | None = None
    pwd: str = field(default="",repr=False)