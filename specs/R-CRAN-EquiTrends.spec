%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EquiTrends
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Equivalence Testing for Pre-Trends in Difference-in-Differences Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-clubSandwich 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-clubSandwich 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-RcppParallel 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Testing for parallel trends is crucial in the Difference-in-Differences
framework. To this end, this package performs equivalence testing in the
context of Difference-in-Differences estimation. It allows users to test
if pre-treatment trends in the treated group are “equivalent” to those in
the control group. Here, “equivalence” means that rejection of the null
hypothesis implies that a function of the pre-treatment placebo effects
(maximum absolute, average or root mean squared value) does not exceed a
pre-specified threshold below which trend differences are considered
negligible. The package is based on the theory developed in Dette &
Schumann (2024) <doi:10.1080/07350015.2024.2308121>.

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
