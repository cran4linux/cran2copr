%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SingRegKrig
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Singularity Regression Kriging for Spatial Prediction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sp 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sp 

%description
Implements the Singularity Regression Kriging ('SRK') model for spatial
prediction by integrating covariate singularity feature construction,
nonlinear trend estimation via random forest, and geostatistical
interpolation of residuals using ordinary kriging. Singularity-based
anomaly indices are computed from environmental covariates at multiple
spatial scales to capture local multiscale heterogeneity and augment the
random forest feature set for trend estimation. The resulting residuals
are interpolated using ordinary kriging to generate final spatial
predictions with uncertainty quantification. Tools for spatial block
cross-validation, parameter sensitivity analysis, and diagnostic
visualization are also provided. Methods are based on Ren, Song, Chen, and
Yu (2026) <doi:10.1080/15481603.2026.2690341>, with singularity theory
from Cheng (2012) <doi:10.1016/j.gexplo.2012.07.007> and Cheng (2017)
<doi:10.1016/j.gr.2017.07.011>, random forest methodology from Breiman
(2001) <doi:10.1023/A:1010933404324>, and regression kriging framework
from Hengl, Heuvelink, and Rossiter (2007)
<doi:10.1016/j.cageo.2007.05.001>.

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
