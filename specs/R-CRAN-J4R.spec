%global packname  J4R
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Create 'Java' Objects and Execute 'Java' Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils >= 3.4.4
Requires:         R-utils >= 3.4.4

%description
Makes it possible to create 'Java' objects and to execute 'Java' methods
from the 'R' environment. The 'Java' Virtual Machine is handled by a
gateway server. Commands are sent to the server through a socket
connection from the 'R' environment. Calls to 'Java' methods allow for
vectors so that a particular method is iteratively run on each element of
the vector. A score algorithm also makes the calls to 'Java' methods less
restrictive. The gateway server relies on the runnable 'Java' library
'j4r.jar'. This library is licensed under the LGPL-3. Its sources are
included in this package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
