import task_manager
import pytest


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
    path = tmp_path / "tasks.json"
    new_id = task_manager.add_task("buy milk", path=path)
    result = task_manager.complete_task(new_id, path=path)
    assert result is True 
    tasks = task_manager.list_tasks(path=path)
    assert tasks[0]["completed"] is True


def test_load_tasks_corrupted_json(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("this is not valid json")
    with pytest.raises(task_manager.CorruptedTasksFileError):
        task_manager.list_tasks(path=path)



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


def test_add_task_empty_string_name(tmp_path):
    path = tmp_path / "tasks.json"
    result = task_manager.add_task("", path=path)
    assert result is None

def test_add_task_new_id_after_delete(tmp_path):
    path = tmp_path / "tasks.json"
    task_manager.add_task("buy milk", path=path)
    id2 = task_manager.add_task("walk dog", path=path)
    id3 = task_manager.add_task("read book", path=path)
    task_manager.delete_task(id2, path=path)
    id4 = task_manager.add_task("new task", path=path)
    assert id4 == 4