%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  merTools
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analyzing Mixed Effect Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1.11
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-blme 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-lme4 >= 1.1.11
Requires:         R-CRAN-arm 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-blme 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-Matrix 

%description
Provides methods for extracting results from mixed-effect model objects
fit with the 'lme4' package. Allows construction of prediction intervals
efficiently from large scale linear and generalized linear mixed-effects
models. This method draws from the simulation framework used in the Gelman
and Hill (2007) textbook: Data Analysis Using Regression and
Multilevel/Hierarchical Models.

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
