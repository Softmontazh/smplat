export default function HomePage() {
  return (
    <div className="space-y-12">
      {/* Hero Section */}
      <section className="text-center space-y-4">
        <h1 className="text-4xl md:text-5xl font-bold text-gray-900">
          Софтмонтаж
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
          Платформа для управления проектами проектирования, монтажа и продажи слаботочных систем
        </p>
        <div className="flex gap-4 justify-center">
          <a href="/dashboard" className="btn btn-primary">
            Перейти в панель
          </a>
          <a href="#about" className="btn btn-outline">
            Узнать больше
          </a>
        </div>
      </section>
      
      {/* Features */}
      <section id="about" className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="card">
          <h3 className="text-lg font-bold mb-3">📋 Управление проектами</h3>
          <p className="text-gray-600">
            Создавайте и отслеживайте все проекты в одном месте
          </p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-bold mb-3">📝 Техническое задание</h3>
          <p className="text-gray-600">
            Формируйте подробные ТЗ для исполнителей
          </p>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-bold mb-3">💰 Сметы и расценки</h3>
          <p className="text-gray-600">
            Быстро создавайте и отправляйте сметы клиентам
          </p>
        </div>
      </section>
    </div>
  )
}
