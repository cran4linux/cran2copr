%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sssvcqr
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse-Smooth Spatially Varying Coefficient Quantile Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 

%description
Implements sparse-smooth spatially varying coefficient quantile regression
(SS-SVCQR), combining quantile regression of Koenker and Bassett (1978)
<doi:10.2307/1913643>, grouped variable selection of Yuan and Lin (2006)
<doi:10.1111/j.1467-9868.2005.00532.x>, graph regularization, and the
alternating direction method of multipliers of Boyd et al. (2011)
<doi:10.1561/2200000016>. The package provides graph-regularized
estimation, spatially blocked cross-validation, prediction, diagnostics,
and simulation helpers for global-local spatial quantile regression.

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
