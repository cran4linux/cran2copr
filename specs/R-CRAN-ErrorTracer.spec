%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ErrorTracer
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Error Propagation and Forecast Uncertainty Decomposition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-brms >= 2.20.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-brms >= 2.20.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a full pipeline from regularized or standard regression models
(elastic net, linear models, generalized linear models, random forests) to
informed Bayesian priors, structured forecast uncertainty decomposition
(parameter / environmental / residual, plus a temporal component when the
model carries an autocorrelation term), and forecast shelf life analysis
(the quantification of when a forecast becomes uninformative). Designed
for ecological and genomic forecasting with climate or environmental
covariates. Methods build on Bürkner (2017) <doi:10.18637/jss.v080.i01>
for Bayesian regression via 'Stan', Friedman, Hastie, and Tibshirani
(2010) <doi:10.18637/jss.v033.i01> for elastic net regularization, Wright
and Ziegler (2017) <doi:10.18637/jss.v077.i01> for random forests, and
Vehtari, Gelman, and Gabry (2017) <doi:10.1007/s11222-016-9696-4> for
leave-one-out cross-validation.

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
