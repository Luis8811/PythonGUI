import enum

class Activity(enum.Enum):
    """Metabolic rates for ANSI/ASHRAE common office activities"""
    person_reading = 1
    person_writing = 1
    person_typing = 1.1
    person_filing_sitting = 1.2
    person_filing_standing = 1.4
    person_walking = 1.7
    person_packing = 2.1
    other = 0

  