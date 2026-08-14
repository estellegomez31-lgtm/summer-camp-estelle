// Adresse du back. En local : vide (le proxy Vite gère /api).
// En production (Render) : définie via la variable d'environnement VITE_API_URL.
export const API = import.meta.env.VITE_API_URL || ''

// --- Session : jeton + membre connecté (gardés en localStorage) ---
let token = localStorage.getItem('token') || ''

export function setToken(t) {
  token = t || ''
  if (t) localStorage.setItem('token', t)
  else localStorage.removeItem('token')
}
export function authHeaders() {
  return token ? { Authorization: 'Bearer ' + token } : {}
}
export function isLogged() { return !!token }

export function setMe(m) {
  if (m) localStorage.setItem('me', JSON.stringify(m))
  else localStorage.removeItem('me')
}
export function getMe() {
  try { return JSON.parse(localStorage.getItem('me') || 'null') } catch (e) { return null }
}
export function logout() { setToken(''); setMe(null) }
