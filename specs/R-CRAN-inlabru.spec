%global packname  inlabru
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Latent Gaussian Modelling using INLA and Extensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.4.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-sp >= 1.4.2
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
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
