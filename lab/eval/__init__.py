"""Evaluation harness: golden cases, audit log, future agent-eval runners."""

from .audit import append_audit, read_audit

__all__ = ["append_audit", "read_audit"]
