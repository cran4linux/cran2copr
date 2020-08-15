%global packname  bsem
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Structural Equation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-visNetwork >= 2.0.9
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.5
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-lattice >= 0.20.38
BuildRequires:    R-CRAN-coda >= 0.19.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-visNetwork >= 2.0.9
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-DiagrammeR >= 1.0.5
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-lattice >= 0.20.38
Requires:         R-CRAN-coda >= 0.19.3
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 

%description
Flexible routines to allow structural equation modeling particular cases
using 'rstan' integration. 'bsem' includes Bayesian semi Confirmatory
Factor Analysis, Confirmatory Factor Analysis, and Structural Equation
Model.  VD Mayrink (2013) <doi:10.1214/12-AOAS607>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
