#
# spec file for package python-requests-stdin
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-requests-stdin
Version:        1.0.0
Release:        0
Summary:        File transport adapter for Requests
License:        Apache-2.0
URL:            https://github.com/huakim/python-requests-stdin
Source:         requests_stdin-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module requests >= 1.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
Requests-Stdin
=============

Requests-Stdin is a transport adapter for use with the `Requests`_ Python
library to allow stdin input access via stdin:\/\/ URLs.

To use:

.. code-block:: python

    import requests
    from requests_stdin import StdinAdapter

    s = requests.Session()
    s.mount('stdin://', StdinAdapter())

    resp = s.get('stdin://some_prompt')

Features
--------

- Will read stdin input
- Might set a Content-Length header
- That's about it

Contributing
------------

Contributions welcome! Feel free to open a pull request against
https://github.com/huakim/requests-stdin

License
-------

To maximise compatibility with Requests, this code is licensed under the Apache
license. See LICENSE for more details.

.. _`Requests`: https://github.com/kennethreitz/requests


%prep
%autosetup -p1 -n requests-stdin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check


%files %{python_files}
%{python_sitelib}/requests-stdin
%{python_sitelib}/requests-stdin-%{version}.dist-info

%changelog
