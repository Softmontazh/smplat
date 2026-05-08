export default function TasksPage() {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Задачи</h1>
        <button className="btn btn-primary">Новая задача</button>
      </div>
      
      <div className="card text-center py-12">
        <p className="text-gray-500">Список задач будет разработан в следующих фазах</p>
      </div>
    </div>
  )
}
