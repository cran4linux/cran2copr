%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  skipTrack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Bayesian Hierarchical Model that Controls for Non-Adherence in Mobile Menstrual Cycle Tracking

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.1.0
BuildRequires:    R-parallel >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-utils >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-LaplacesDemon >= 16.0.0
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-mvtnorm >= 1.2.0
BuildRequires:    R-CRAN-doParallel >= 1.0.0
BuildRequires:    R-CRAN-genMCMCDiag >= 0.2.0
BuildRequires:    R-CRAN-optimg >= 0.1.2
BuildRequires:    R-CRAN-ggtext >= 0.1.0
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-glmnet >= 4.1.0
Requires:         R-parallel >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-utils >= 4.0.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-LaplacesDemon >= 16.0.0
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-mvtnorm >= 1.2.0
Requires:         R-CRAN-doParallel >= 1.0.0
Requires:         R-CRAN-genMCMCDiag >= 0.2.0
Requires:         R-CRAN-optimg >= 0.1.2
Requires:         R-CRAN-ggtext >= 0.1.0
Requires:         R-CRAN-lifecycle 

%description
Implements a Bayesian hierarchical model designed to identify skips in
mobile menstrual cycle self-tracking on mobile apps. Future developments
will allow for the inclusion of covariates affecting cycle mean and
regularity, as well as extra information regarding tracking non-adherence.
Main methods to be outlined in a forthcoming paper, with alternative
models from Li et al. (2022) <doi:10.1093/jamia/ocab182>.

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
