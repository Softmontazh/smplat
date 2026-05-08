export default function Footer() {
  const currentYear = new Date().getFullYear()
  
  return (
    <footer className="bg-gray-900 text-gray-300 mt-12">
      <div className="max-w-7xl mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Company Info */}
          <div>
            <h3 className="text-white font-bold mb-4">ТОО Софтмонтаж</h3>
            <p className="text-sm mb-4">
              Проектирование, монтаж и продажа слаботочных систем
            </p>
            <p className="text-sm">
              <a href="mailto:info@softmontazh.kz" className="hover:text-white">
                info@softmontazh.kz
              </a>
            </p>
          </div>
          
          {/* Quick Links */}
          <div>
            <h4 className="text-white font-semibold mb-4">Навигация</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="/" className="hover:text-white">Главная</a></li>
              <li><a href="/projects" className="hover:text-white">Проекты</a></li>
              <li><a href="/tasks" className="hover:text-white">Задачи</a></li>
            </ul>
          </div>
          
          {/* Legal */}
          <div>
            <h4 className="text-white font-semibold mb-4">Информация</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-white">Политика конфиденциальности</a></li>
              <li><a href="#" className="hover:text-white">Условия использования</a></li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-800 mt-8 pt-8 text-center text-sm">
          <p>&copy; {currentYear} ТОО Софтмонтаж. Все права защищены.</p>
        </div>
      </div>
    </footer>
  )
}
