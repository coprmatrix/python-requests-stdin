my $name = <<'EOF';
%files -n %{python_name}
%{python3_sitelib}/requests_stdin-%{version}.dist-info
%{python3_sitelib}/requests_stdin.py
%{python3_sitelib}/__pycache__/*
EOF

s/%files -n %{python_name}.*/${name}/g;
