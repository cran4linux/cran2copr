%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  webSDM
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Including Known Interactions in Species Distribution Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jtools 
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-CRAN-rstantools 
BuildRequires:    R-utils 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jtools 
Requires:         R-CRAN-rstanarm 
Requires:         R-CRAN-rstantools 
Requires:         R-utils 

%description
A collection of tools to fit and work with trophic Species Distribution
Models. Trophic Species Distribution Models combine knowledge of trophic
interactions with Bayesian structural equation models that model each
species as a function of its prey (or predators) and environmental
conditions. It exploits the topological ordering of the known trophic
interaction network to predict species distribution in space and/or time,
where the prey (or predator) distribution is unavailable. The method
implemented by the package is described in Poggiato, Andréoletti, Pollock
and Thuiller (2022) <doi:10.22541/au.166853394.45823739/v1>.

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
