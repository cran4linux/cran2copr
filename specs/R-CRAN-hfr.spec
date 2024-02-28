%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hfr
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Hierarchical Feature Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-quadprog 
Requires:         R-stats 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-corpcor 

%description
Provides functions for the estimation, plotting, predicting and
cross-validation of hierarchical feature regression models as described in
Pfitzinger (2024). Cluster Regularization via a Hierarchical Feature
Regression. Econometrics and Statistics (in press).
<doi:10.1016/j.ecosta.2024.01.003>.

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
