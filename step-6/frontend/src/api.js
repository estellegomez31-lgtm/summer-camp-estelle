const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function api(path, options = {}) {
  const url = API + path;
  const r = await fetch(url, options);
  return r.json();
}
