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


def test_complete_task_success(tmp_path):
    path = tmp_path / "tasjs.json"
    new_id = task_manager.add_task("buy milk", path=path)
    result = task_manager.complete_task(new_id, path=path)
    assert result is True 
    tasks = task_manager.list_tasks(path=path)
    assert tasks[0]["completed"] is True


def test_complete_task_missing_id(tmp_path):
    path = tmp_path / "tasks.json"
    task_manager.add_task("buy milk", path=path)
    result = task_manager.complete_task(9999, path=path)
    assert result is False
    tasks = task_manager.list_tasks(path=path)
    assert tasks[0]["completed"] is False


def test_list_tasks_empty(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = task_manager.list_tasks(path=path)
    assert tasks == []