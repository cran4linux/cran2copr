%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  admixr2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Aggregate Data Modelling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-nlmixr2est 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-qs2 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rxode2 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-nlmixr2est 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-qs2 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rxode2 

%description
Fit pharmacokinetic/pharmacodynamic (PK/PD) models to aggregate-level data
(mean vector and covariance matrix per study) rather than individual-level
data. Integrates with the 'nlmixr2'/'rxode2' ecosystem via three
estimation methods: a First-Order ('FO') analytical estimator, a Monte
Carlo (MC) estimator, and an Iterative Reweighting Monte Carlo ('IRMC')
estimator. Methods are based on Välitalo (2021)
<doi:10.1007/s10928-021-09760-1>; software described in van de Beek et al.
(2025) <doi:10.1007/s10928-025-10011-w>.

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
