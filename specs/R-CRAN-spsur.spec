%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spsur
%global packver   1.0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Seemingly Unrelated Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.56
BuildRequires:    R-methods >= 4.1
BuildRequires:    R-stats >= 4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-gmodels >= 2.18.1
BuildRequires:    R-CRAN-sphet >= 2.0
BuildRequires:    R-CRAN-Matrix >= 1.4.1
BuildRequires:    R-CRAN-spatialreg >= 1.2.5
BuildRequires:    R-CRAN-spdep >= 1.2.5
BuildRequires:    R-CRAN-Formula >= 1.2.4
BuildRequires:    R-CRAN-minqa >= 1.2.4
BuildRequires:    R-CRAN-rlang >= 1.0.4
BuildRequires:    R-CRAN-sparseMVN >= 0.2.2
Requires:         R-CRAN-MASS >= 7.3.56
Requires:         R-methods >= 4.1
Requires:         R-stats >= 4.1
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-gmodels >= 2.18.1
Requires:         R-CRAN-sphet >= 2.0
Requires:         R-CRAN-Matrix >= 1.4.1
Requires:         R-CRAN-spatialreg >= 1.2.5
Requires:         R-CRAN-spdep >= 1.2.5
Requires:         R-CRAN-Formula >= 1.2.4
Requires:         R-CRAN-minqa >= 1.2.4
Requires:         R-CRAN-rlang >= 1.0.4
Requires:         R-CRAN-sparseMVN >= 0.2.2

%description
A collection of functions to test and estimate Seemingly Unrelated
Regression (usually called SUR) models, with spatial structure, by maximum
likelihood and three-stage least squares. The package estimates the most
common spatial specifications, that is, SUR with Spatial Lag of X
regressors (called SUR-SLX), SUR with Spatial Lag Model (called SUR-SLM),
SUR with Spatial Error Model (called SUR-SEM), SUR with Spatial Durbin
Model (called SUR-SDM), SUR with Spatial Durbin Error Model (called
SUR-SDEM), SUR with Spatial Autoregressive terms and Spatial
Autoregressive Disturbances (called SUR-SARAR), SUR-SARAR with Spatial Lag
of X regressors (called SUR-GNM) and SUR with Spatially Independent Model
(called SUR-SIM). The methodology of these models can be found in next
references Mur, J., Lopez, F., and Herrera, M. (2010)
<doi:10.1080/17421772.2010.516443> Lopez, F.A., Mur, J., and Angulo, A.
(2014) <doi:10.1007/s00168-014-0624-2>.

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
