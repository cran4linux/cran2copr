%global __brp_check_rpaths %{nil}
%global packname  eicm
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Explicit Interaction Community Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-GA >= 3.1
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-optimParallel 
Requires:         R-CRAN-GA >= 3.1
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-optimParallel 

%description
Model fitting and species biotic interaction network topology selection
for explicit interaction community models. Explicit interaction community
models are an extension of binomial linear models for joint modelling of
species communities, that incorporate both the effects of species biotic
interactions and the effects of missing covariates. Species interactions
are modelled as direct effects of each species on each of the others, and
are estimated alongside the effects of missing covariates, modelled as
latent factors. The package includes a penalized maximum likelihood
fitting function, and a genetic algorithm for selecting the most
parsimonious species interaction network topology.

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
