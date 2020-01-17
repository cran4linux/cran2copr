%global packname  dbmss
%global packver   2.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.1
Release:          1%{?dist}
Summary:          Distance-Based Measures of Spatial Structures

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
Requires:         pandoc
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-spatstat.utils >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-spatstat.utils >= 1.3.1
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-tibble 

%description
Simple computation of spatial statistic functions of distance to
characterize the spatial structures of mapped objects, following Marcon,
Traissac, Puech, and Lang (2015) <doi:10.18637/jss.v067.c03>. Includes
classical functions (Ripley's K and others) and more recent ones used by
spatial economists (Duranton and Overman's Kd, Marcon and Puech's M).
Relies on 'spatstat' for some core calculation.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
