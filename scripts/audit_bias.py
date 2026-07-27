"""
scripts/audit_bias.py — PathReview

Offline bias audit script: samples stored reviews, runs them through
BiasDetector, and produces a report showing flag rates by signal type.

Issue #72: https://github.com/ascherj/pathreview/issues/72

STATUS: Stub — implementation in progress (Week 9).

Reproduction note:
    Running this script currently produces no output because the implementation
    is missing. BiasDetector exists in safety/bias_detector.py and is fully
    functional, but is never called in a batch/offline context. This script
    is the missing piece.

    To confirm the gap:
        python scripts/audit_bias.py
    Expected: a report showing bias flag rates across sampled reviews
    Actual: NotImplementedError
"""

import asyncio

import structlog

logger = structlog.get_logger()


async def main() -> None:
    raise NotImplementedError(
        "audit_bias.py is not yet implemented. "
        "See PLAN.md for the solution approach. "
        "Issue: https://github.com/ascherj/pathreview/issues/72"
    )


if __name__ == "__main__":
    asyncio.run(main())
