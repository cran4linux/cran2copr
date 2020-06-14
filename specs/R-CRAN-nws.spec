%global packname  nws
%global packver   1.7.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0.1
Release:          2%{?dist}
Summary:          R functions for NetWorkSpaces and Sleigh

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1
Requires:         R-core >= 2.1
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Provides coordination and parallel execution facilities, as well as
limited cross-language data exchange, using the netWorkSpaces server
developed by REvolution Computing

%prep
%setup -q -c -n %{packname}
find %{packname}/inst -type f -exec sed -Ei 's@#!/usr/bin/(env )*python@#!/usr/bin/python2@g' {} \;

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bin
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/README.sleigh
%{rlibdir}/%{packname}/INDEX
