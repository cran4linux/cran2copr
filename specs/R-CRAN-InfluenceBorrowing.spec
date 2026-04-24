%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  InfluenceBorrowing
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Influence-Based Borrowing for Hybrid Control Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-KRLS 
BuildRequires:    R-stats 
Requires:         R-CRAN-KRLS 
Requires:         R-stats 

%description
Implements the adaptive influence-based borrowing framework proposed by
Qinwei Yang, Jingyi Li, Peng Wu, and Shu Yang (2026+) in the paper
``Improving Treatment Effect Estimation in Trials through Adaptive
Borrowing of External Controls" <doi:10.48550/arXiv.2604.13973> for
augmenting Randomized Controlled Trials (RCTs) with External Control (EC)
data. This package provides a comprehensive workflow to: (1) quantify the
comparability of external control samples using influence scores
approximated via the influence function of the M-estimator; (2) construct
candidate borrowing subsets and select the optimal subset that minimizes
the Mean Squared Error (MSE); and (3) calibrate systematic differences in
external outcomes using R-learner methods implemented via Ordinary Least
Squares or Kernel Ridge Regression.

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
