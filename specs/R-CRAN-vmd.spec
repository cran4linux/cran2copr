%global packname  vmd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Variational Mode Decomposition

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-ggplot2 >= 2.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-R6 

%description
A port and extension to the original 'Matlab' code made public by
Dragomiretskiy and Zosso, for conducting Variational Mode Decomposition
(VMD) as described within their 2013 publication (publication:
<doi:10.1109/TSP.2013.2288675>, source: <https://goo.gl/fJH1d5>).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
