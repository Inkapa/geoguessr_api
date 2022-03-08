from dataclasses import dataclass, field
from dataclass_wizard import JSONWizard


@dataclass
class Invoice(JSONWizard):
    id: str
    date: str
    paid: bool
    invoice_url: str = field(init=False)

    def __post_init__(self):
        self.invoice_url = f"https://www.geoguessr.com/me/invoices/{self.id}"


@dataclass
class Subscription(JSONWizard):
    id: str
    type: int
    pay_provider: int
    created: str
    plan: str
    plan_id: str
    cost: float
    currency: str
    started: str
    started_at: str
    trial_end: str
    trial_ending_at: str
    period_ends_at: str
    period_ending_at: str
    canceled: bool
    interval: int
    member_limit: int
    product: int
    is_active: bool
    is_in_trial_period: bool
