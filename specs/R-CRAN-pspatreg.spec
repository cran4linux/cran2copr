%global __brp_check_rpaths %{nil}
%global packname  pspatreg
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Spatio-Temporal Semiparametric Regression Models with Spatial Lags

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-grDevices >= 4.1.2
BuildRequires:    R-methods >= 4.1
BuildRequires:    R-stats >= 4.1
BuildRequires:    R-graphics >= 4.1
BuildRequires:    R-splines >= 4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-plm >= 2.6.1
BuildRequires:    R-CRAN-Rdpack >= 2.1
BuildRequires:    R-CRAN-fields >= 13.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-Matrix >= 1.3.4
BuildRequires:    R-CRAN-minqa >= 1.2.4
BuildRequires:    R-CRAN-spatialreg >= 1.2.3
BuildRequires:    R-CRAN-spdep >= 1.2.2
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-sf >= 1.0.7
BuildRequires:    R-CRAN-MBA >= 0.0.9
BuildRequires:    R-CRAN-AmesHousing >= 0.0.4
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-grDevices >= 4.1.2
Requires:         R-methods >= 4.1
Requires:         R-stats >= 4.1
Requires:         R-graphics >= 4.1
Requires:         R-splines >= 4.1
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-plm >= 2.6.1
Requires:         R-CRAN-Rdpack >= 2.1
Requires:         R-CRAN-fields >= 13.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-Matrix >= 1.3.4
Requires:         R-CRAN-minqa >= 1.2.4
Requires:         R-CRAN-spatialreg >= 1.2.3
Requires:         R-CRAN-spdep >= 1.2.2
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-sf >= 1.0.7
Requires:         R-CRAN-MBA >= 0.0.9
Requires:         R-CRAN-AmesHousing >= 0.0.4

%description
Estimation and inference of spatial and spatio-temporal semiparametric
models including spatial or spatio-temporal non-parametric trends,
parametric and non-parametric covariates and, possibly, a spatial lag for
the dependent variable and temporal correlation in the noise. The
spatio-temporal trend can be decomposed in ANOVA way including main and
interaction functional terms. Use of SAP algorithm to estimate the spatial
or spatio-temporal trend and non-parametric covariates. The methodology of
these models can be found in next references Basile, R. et al. (2014),
<doi:10.1016/j.jedc.2014.06.011>; Rodriguez-Alvarez, M.X. et al. (2015)
<doi:10.1007/s11222-014-9464-2> and, particularly referred to the focus of
the package, Minguez, R., Basile, R. and Durban, M. (2020)
<doi:10.1007/s10260-019-00492-8>.

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
