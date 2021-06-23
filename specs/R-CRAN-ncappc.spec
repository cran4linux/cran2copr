%global __brp_check_rpaths %{nil}
%global packname  ncappc
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          NCA Calculations and Population Model Diagnosis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.0.0
BuildRequires:    R-CRAN-readr >= 0.2.2
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-PopED 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bookdown 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-gridExtra >= 2.0.0
Requires:         R-CRAN-readr >= 0.2.2
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-PopED 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-tidyr 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-bookdown 

%description
A flexible tool that can perform (i) traditional non-compartmental
analysis (NCA) and (ii) Simulation-based posterior predictive checks for
population pharmacokinetic (PK) and/or pharmacodynamic (PKPD) models using
NCA metrics.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
