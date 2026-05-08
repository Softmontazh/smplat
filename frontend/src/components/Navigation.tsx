import { Link } from 'react-router-dom'
import { useAuthStore } from '../store/authStore'

export default function Navigation() {
  const { user, isAuthenticated, logout } = useAuthStore()
  
  return (
    <nav className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center gap-2">
            <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">СМ</span>
            </div>
            <span className="font-bold text-lg hidden sm:inline">Софтмонтаж</span>
          </Link>
          
          {/* Menu */}
          <div className="hidden md:flex gap-8">
            <Link to="/" className="text-gray-700 hover:text-blue-600">Главная</Link>
            {isAuthenticated && (
              <>
                <Link to="/dashboard" className="text-gray-700 hover:text-blue-600">Панель</Link>
                <Link to="/projects" className="text-gray-700 hover:text-blue-600">Проекты</Link>
                <Link to="/tasks" className="text-gray-700 hover:text-blue-600">Задачи</Link>
                <Link to="/quotes" className="text-gray-700 hover:text-blue-600">Сметы</Link>
              </>
            )}
          </div>
          
          {/* User Menu */}
          <div className="flex items-center gap-4">
            {isAuthenticated && user ? (
              <div className="flex items-center gap-4">
                <span className="text-sm text-gray-700 hidden sm:inline">
                  {user.first_name} {user.last_name}
                </span>
                <button 
                  onClick={logout}
                  className="text-sm text-gray-700 hover:text-blue-600"
                >
                  Выход
                </button>
              </div>
            ) : (
              <Link to="/login" className="text-sm font-medium text-blue-600 hover:text-blue-700">
                Вход
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  )
}
