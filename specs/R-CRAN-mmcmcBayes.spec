%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmcmcBayes
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multistage MCMC Method for Detecting DMRs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack >= 1.4.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-MCMCpack >= 1.4.0
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements differential methylation region (DMR) detection using a
multistage Markov chain Monte Carlo (MCMC) algorithm based on the
alpha-skew generalized normal (ASGN) distribution. Version 0.2.0 removes
the Anderson-Darling test stage, improves computational efficiency of the
core ASGN and multistage MCMC routines, and adds convenience functions for
summarizing and visualizing detected DMRs. The methodology is based on
Yang (2025) <https://www.proquest.com/docview/3218878972>.

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
