%global packname  opart
%global packver   2019.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.1.0
Release:          1%{?dist}
Summary:          Optimal Partitioning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
A reference implementation of standard optimal partitioning algorithm in C
using square-error loss and Poisson loss functions as described by Robert
Maidstone (2016) <doi:10.1007/s11222-016-9636-3>, Toby Hocking (2016)
<doi:10.1007/s11222-016-9636-3>, Guillem Rigaill (2016)
<doi:10.1007/s11222-016-9636-3>, Paul Fearnhead (2016)
<doi:10.1007/s11222-016-9636-3>. It scales quadratically with number of
data points in terms of time-complexity.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
