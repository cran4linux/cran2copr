%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppmlasso
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Point Process Models with LASSO-Type Penalties

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.model 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat >= 3.0.0
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lattice 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.model 
Requires:         R-CRAN-spatstat.geom 

%description
Toolkit for fitting point process models with sequences of LASSO penalties
("regularisation paths"), as described in Renner, I.W. and Warton, D.I.
(2013) <doi:10.1111/j.1541-0420.2012.01824.x>. Regularisation paths of
Poisson point process models or area-interaction models can be fitted with
LASSO, adaptive LASSO or elastic net penalties. A number of criteria are
available to judge the bias-variance tradeoff.

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
