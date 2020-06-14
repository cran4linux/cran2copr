%global packname  bayes4psy
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          2%{?dist}
Summary:          User Friendly Bayesian Data Analysis for Psychology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rstan >= 2.17.3
BuildRequires:    R-CRAN-StanHeaders >= 2.17.2
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-rstantools >= 1.5.0
BuildRequires:    R-CRAN-mcmcse >= 1.3.2
BuildRequires:    R-CRAN-emg >= 1.0.7
BuildRequires:    R-CRAN-cowplot >= 0.9.3
BuildRequires:    R-CRAN-metRology >= 0.9.28
BuildRequires:    R-CRAN-reshape >= 0.8.7
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-circular >= 0.4.93
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rstan >= 2.17.3
Requires:         R-CRAN-rstantools >= 1.5.0
Requires:         R-CRAN-mcmcse >= 1.3.2
Requires:         R-CRAN-emg >= 1.0.7
Requires:         R-CRAN-cowplot >= 0.9.3
Requires:         R-CRAN-metRology >= 0.9.28
Requires:         R-CRAN-reshape >= 0.8.7
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-circular >= 0.4.93
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains several Bayesian models for data analysis of psychological tests.
A user friendly interface for these models should enable students and
researchers to perform professional level Bayesian data analysis without
advanced knowledge in programming and Bayesian statistics. This package is
based on the Stan platform (Carpenter et el. 2017
<doi:10.18637/jss.v076.i01>).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
