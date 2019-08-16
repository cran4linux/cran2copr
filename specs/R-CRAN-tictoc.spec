%global packname  tictoc
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Functions for timing R scripts, as well as implementations ofStack and List structures.

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
This package provides the timing functions 'tic' and 'toc' that can be
nested. One can record all timings while a complex script is running, and
examine the values later. It is also possible to instrument the timing
calls with custom callbacks. In addition, this package provides class
'Stack', implemented as a vector, and class 'List', implemented as a list,
both of which support operations 'push', 'pop', 'first', 'last' and
'clear'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/genpdfdoc.sh
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/tictoc_1.0.pdf
%{rlibdir}/%{packname}/INDEX
