%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobustCalibration
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Calibration of Imperfect Mathematical Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-nloptr >= 1.0.4
BuildRequires:    R-CRAN-RobustGaSP >= 0.6.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-nloptr >= 1.0.4
Requires:         R-CRAN-RobustGaSP >= 0.6.4
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-methods 

%description
Implements full Bayesian analysis for calibrating mathematical models with
new methodology for modeling the discrepancy function. It allows for
emulation, calibration and prediction using complex mathematical model
outputs and experimental data. See the reference: Mengyang Gu and Long
Wang (2018) <arXiv:1707.08215>, Mengyang Gu, Fangzheng Xie and Long Wang
(2021) <arXiv:1807.03829>, Mengyang Gu, Kyle Anderson and Erika McPhillips
(2021) <arXiv:1810.11664>.

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
