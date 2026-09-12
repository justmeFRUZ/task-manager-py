import task_manager

def test_add_task_return_new_id(tmp_path):
    path = tmp_path / "tasks.json"
    new_id = task_manager.add_task("buy milk", path=path)
    assert new_id == 1
