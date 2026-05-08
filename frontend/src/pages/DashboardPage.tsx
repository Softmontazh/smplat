export default function DashboardPage() {
  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Панель управления</h1>
      
      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="card">
          <div className="text-sm text-gray-600 mb-2">Всего проектов</div>
          <div className="text-3xl font-bold">0</div>
        </div>
        <div className="card">
          <div className="text-sm text-gray-600 mb-2">Активных задач</div>
          <div className="text-3xl font-bold">0</div>
        </div>
        <div className="card">
          <div className="text-sm text-gray-600 mb-2">Сметы в ожидании</div>
          <div className="text-3xl font-bold">0</div>
        </div>
        <div className="card">
          <div className="text-sm text-gray-600 mb-2">Общий доход</div>
          <div className="text-3xl font-bold">0 ₸</div>
        </div>
      </div>
      
      {/* Placeholder */}
      <div className="card text-center py-12">
        <p className="text-gray-500">
          Панель управления будет разработана в Фазе 4
        </p>
      </div>
    </div>
  )
}
