"""Deployment boundary tests for the Vercel Python entrypoint."""


def test_serverless_entrypoint_exposes_the_working_vetproof_handler():
    """A deployment must route requests through the same UI/API handler as local use."""
    from api.index import handler
    from server import Handler

    assert handler is Handler


def test_serverless_flow_uses_configured_writable_runtime_directories(tmp_path, monkeypatch):
    """A serverless run must not attempt receipts or effects in the read-only bundle."""
    monkeypatch.setenv("VERCEL", "1")
    monkeypatch.setenv("AEVION_STATE_DIR", str(tmp_path))

    from app.agent import StopAndAskFlow

    flow = StopAndAskFlow()

    assert flow.state_dir == tmp_path / "receipts"
    assert flow.output_dir == tmp_path / "output"
