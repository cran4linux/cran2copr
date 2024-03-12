%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nonmem2R
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Loading NONMEM Output Files with Functions for Visual Predictive Checks (VPC) and Goodness of Fit (GOF) Plots

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-splines2 
Requires:         R-CRAN-reshape2 

%description
Loading NONMEM (NONlinear Mixed-Effect Modeling,
<https://www.iconplc.com/solutions/technologies/nonmem/>) and PSN
(Perl-speaks-NONMEM, <https://uupharmacometrics.github.io/PsN/>) output
files to extract parameter estimates, provide visual predictive check
(VPC) and goodness of fit (GOF) plots, and simulate with parameter
uncertainty.

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
