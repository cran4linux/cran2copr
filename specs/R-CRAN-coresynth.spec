%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coresynth
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Unified Synthetic Control Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-jsonlite 

%description
A unified 'Formula' interface to the Synthetic Control Method (SCM) and
related panel-data causal inference estimators: Synthetic
Difference-in-Differences (SDID), Generalized Synthetic Control (GSC),
Matrix Completion (MC), Time-Aware Synthetic Control (TASC), and Synthetic
Interventions (SI), together with an experimental-design variant.
Computational bottlenecks (quadratic programming, singular value
decomposition, and Kalman filtering) are implemented in 'C++' via
'RcppArmadillo'. Methods are described in Abadie, Diamond and Hainmueller
(2010) <doi:10.1198/jasa.2009.ap08746>, Arkhangelsky, Athey, Hirshberg,
Imbens and Wager (2021) <doi:10.1257/aer.20190159>, Xu (2017)
<doi:10.1017/pan.2016.2>, Athey, Bayati, Doudchenko, Imbens and Khosravi
(2021) <doi:10.1080/01621459.2021.1891924>, and Agarwal, Shah and Shen
(2025) <doi:10.1287/opre.2025.1590>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
