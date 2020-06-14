%global packname  SEERaBomb
%global packver   2019.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.2
Release:          2%{?dist}
Summary:          SEER and Atomic Bomb Survivor Data Analysis Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-demography 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-LaF 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-WriteXLS 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-survival 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-demography 
Requires:         R-CRAN-reshape2 
Requires:         R-mgcv 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-LaF 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-WriteXLS 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-survival 

%description
Creates SEER (Surveillance, Epidemiology and End Results) and A-bomb data
binaries from ASCII sources and provides tools for estimating SEER second
cancer risks. Methods are described in <doi:10.1038/leu.2015.258>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/docs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
