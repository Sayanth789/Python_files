from dataclass import dataclass, field 

@dataclass
class ClubMember:
    name: str 
    guests: list[str]= field(default_factory=list)

    