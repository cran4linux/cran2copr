%global packname  RcppDate
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          'date' C++ Header Library for Date and Time Functionality

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
'date' is a C++ header library offering extensive date and time
functionality for the C++11, C++14 and C++17 standards written by Howard
Hinnant and released under the MIT license. A slightly modified version
has been accepted (along with 'tz.h') as part of C++20. This package
regroups all header files from the upstream repository by Howard Hinnant
so that other R packages can use them in their C++ code. At present, few
of the types have explicit 'Rcpp' wrapper though these may be added as
needed.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
