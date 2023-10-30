%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inlabru
%global packver   2.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Latent Gaussian Modelling using INLA and Extensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.4.5
BuildRequires:    R-CRAN-fmesher >= 0.1.2
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MatrixModels 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-sp >= 1.4.5
Requires:         R-CRAN-fmesher >= 0.1.2
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MatrixModels 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Facilitates spatial and general latent Gaussian modeling using integrated
nested Laplace approximation via the INLA package
(<https://www.r-inla.org>). Additionally, extends the GAM-like model class
to more general nonlinear predictor expressions, and implements a log
Gaussian Cox process likelihood for modeling univariate and spatial point
processes based on ecological survey data. Model components are specified
with general inputs and mapping methods to the latent variables, and the
predictors are specified via general R expressions, with separate
expressions for each observation likelihood model in multi-likelihood
models. A prediction method based on fast Monte Carlo sampling allows
posterior prediction of general expressions of the latent variables.
Ecology-focused introduction in Bachl, Lindgren, Borchers, and Illian
(2019) <doi:10.1111/2041-210X.13168>.

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
