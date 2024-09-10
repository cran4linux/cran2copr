%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jtdm
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Modelling of Functional Traits

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-mniw 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-mniw 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 

%description
Fitting and analyzing a Joint Trait Distribution Model. The Joint Trait
Distribution Model is implemented in the Bayesian framework using
conjugate priors and posteriors, thus guaranteeing fast inference. In
particular the package computes joint probabilities and multivariate
confidence intervals, and enables the investigation of how they depend on
the environment through partial response curves. The method implemented by
the package is described in Poggiato et al. (2023)
<doi:10.1111/geb.13706>.

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
