from typing import List, Optional
from pydantic import BaseModel, Field



class TransactionBase(BaseModel):
    TransactionID: str = Field(..., example="TXN_001")

    TransactionAmt: float = Field(
        ...,
        gt=0,
        example=1250.75,
        description="Transaction amount"
    )

    TransactionDT: int = Field(
        ...,
        ge=0,
        example=864000,
        description="Seconds since reference time"
    )

    card1: int = Field(
        ...,
        example=12345,
        description="Primary card identifier"
    )

    addr1: Optional[int] = Field(
        None,
        example=210,
        description="Billing address identifier"
    )

    DeviceType: Optional[str] = Field(
        None,
        example="desktop",
        description="Type of device used"
    )

    DeviceInfo: Optional[str] = Field(
        None,
        example="Windows_Chrome",
        description="Device fingerprint information"
    )



class SinglePredictionRequest(TransactionBase):
    pass



class BatchPredictionRequest(BaseModel):
    transactions: List[TransactionBase]

    class Config:
        schema_extra = {
            "example": {
                "transactions": [
                    {
                        "TransactionID": "TXN_001",
                        "TransactionAmt": 1250.75,
                        "TransactionDT": 864000,
                        "card1": 12345,
                        "addr1": 210,
                        "DeviceType": "desktop",
                        "DeviceInfo": "Windows_Chrome"
                    },
                    {
                        "TransactionID": "TXN_002",
                        "TransactionAmt": 75.50,
                        "TransactionDT": 864120,
                        "card1": 67890,
                        "addr1": 315,
                        "DeviceType": "mobile",
                        "DeviceInfo": "Android_Chrome"
                    }
                ]
            }
        }



class PredictionResult(BaseModel):
    TransactionID: str

    risk_level: str = Field(
        ...,
        example="High Risk"
    )

    reasons: List[str] = Field(
        ...,
        example=[
            "Multiple transactions in a short time",
            "Amount unusually high compared to past behavior"
        ]
    )

    recommended_action: str = Field(
        ...,
        example="Hold transaction and request verification"
    )


class BatchPredictionResponse(BaseModel):
    results: List[PredictionResult]
