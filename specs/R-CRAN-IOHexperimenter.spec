%global packname  IOHexperimenter
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Benchmarking Part of the 'IOHprofiler'

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-magrittr 

%description
The benchmarking module for the Iterative Optimization Heuristics Profiler
('IOHprofiler'). This module provides benchmarking in the 'IOHprofiler'
format, which can be visualized using the 'IOHanalyzer' module.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
