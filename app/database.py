{% if session["user"] %}
    <h2>Welcome, {{ session["user"] }}!</h2>
    <a href="{{ url_for('logout') }}">Logout</a>
{% else %}
    <p>You are not logged in.</p>
    <a href="{{ url_for('login') }}">Login</a>
{% endif %}
