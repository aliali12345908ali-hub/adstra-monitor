from fastapi import FastAPI, HTTPException
import stripe

app = FastAPI()

# تعريف الباقات الفاخرة والخدمات عالية الجودة
SERVICES_TIERS = {
    "silver": {
        "name": "Silver Sovereign Tier",
        "price_eur": 1500,
        "description": "Standard Autonomous Setup & Basic Security Shield.",
    },
    "gold": {
        "name": "Gold Empire Tier",
        "price_eur": 5000,
        "description": (
            "Advanced Automation, Live Revenue Tracking & Priority Support."
        ),
    },
    "diamond": {
        "name": "Diamond Ultimate Empire Tier",
        "price_eur": 12000,
        "description": (
            "Full Custom Autonomous OS, 24/7 Dedicated Sovereign Security &"
            " Instant Bank Routing."
        ),
    },
}


@app.get("/api/get-service-tier")
def get_service_tier(tier_key: str):
  if tier_key not in SERVICES_TIERS:
    raise HTTPException(
        status_code=404, detail="Service tier not found or invitation required."
    )

  tier = SERVICES_TIERS[tier_key]
  return {
      "status": "success",
      "tier_name": tier["name"],
      "investment_required_eur": tier["price_eur"],
      "details": tier["description"],
      "policy": (
          "Payment First: Access and deployment begin strictly after verified"
          " Stripe transaction."
      ),
  }


if __name__ == "__main__":
  print(
      "🚀 [Adastra Empire] - High-Ticket Service Tiers & Subscriptions"
      " Initialized."
  )

