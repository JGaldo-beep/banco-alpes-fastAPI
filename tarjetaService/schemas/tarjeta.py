from typing import Optional
from pydantic import BaseModel, Field

class Tarjeta(BaseModel):
    id: Optional[int] = None
    name_card: str
    card_type: str
    main_benefits: str
    annual_percentage_rate: float
    annual_fee: float
    minimum_requirements: str
    payments_options: str
    credit_limit: float
    apply_online: bool
    
    # title: str = Field(min_length = 5, max_length = 15)
    # overview: str = Field(min_length = 15, max_length = 30)
    # year: int = Field(le = 2022)
    # rating: float
    # category: str
    
    