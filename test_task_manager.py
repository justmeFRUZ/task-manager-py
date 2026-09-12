import task_manager

def test_add_task_return_new_id(tmp_path):
    path = tmp_path / "tasks.json"
    new_id = task_manager.add_task("buy milk", path=path)
    assert new_id == 1

def test_list_tasks_with_task(tmp_path):
    path = tmp_path / "tasks.json"
    task_manager.add_task("buy milk", path=path)
    tasks = task_manager.list_tasks(path=path)
    assert len(tasks) == 1
    assert tasks[0]["description"] == "buy milk"


def test_list_tasks_empty(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = task_manager.list_tasks(path=path)
    assert tasks == []