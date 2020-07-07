%global packname  thurstonianIRT
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          2%{?dist}
Summary:          Thurstonian IRT Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-rstan >= 2.17.3
BuildRequires:    R-CRAN-StanHeaders >= 2.17.2
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-rstantools >= 1.5.0
BuildRequires:    R-CRAN-tibble >= 1.3.1
BuildRequires:    R-CRAN-lavaan >= 0.6.1
BuildRequires:    R-CRAN-dplyr >= 0.6.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-rstan >= 2.17.3
Requires:         R-CRAN-rstantools >= 1.5.0
Requires:         R-CRAN-tibble >= 1.3.1
Requires:         R-CRAN-lavaan >= 0.6.1
Requires:         R-CRAN-dplyr >= 0.6.0
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-methods 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Fit Thurstonian Item Response Theory (IRT) models in R. This package
supports fitting Thurstonian IRT models and its extensions using 'Stan',
'lavaan', or 'Mplus' for the model estimation. Functionality for
extracting results and simulating data is provided as well. References:
Brown & Maydeu-Olivares (2011) <doi:10.1177/0013164410375112>; Bürkner et
al. (2019) <doi:10.1177/0013164419832063>.

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
