%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdbma
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Mediation Analysis with High-Dimensional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-survival 
Requires:         R-splines 
Requires:         R-CRAN-lattice 
Requires:         R-methods 

%description
Mediation analysis is used to identify and quantify intermediate effects
from factors that intervene the observed relationship between an
exposure/predicting variable and an outcome. We use a Bayesian adaptive
lasso method to take care of the hierarchical structures and high
dimensional exposures or mediators.

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
