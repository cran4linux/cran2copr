%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jlme
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Modelling with 'GLM.jl' and 'MixedModels.jl' in 'Julia'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-JuliaConnectoR 
BuildRequires:    R-CRAN-JuliaFormulae 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-JuliaConnectoR 
Requires:         R-CRAN-JuliaFormulae 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 

%description
Bindings to 'Julia' packages 'GLM.jl' <doi:10.5281/zenodo.3376013> and
'MixedModels.jl' <doi:10.5281/zenodo.12575371>, powered by
'JuliaConnectoR'. Fits (generalized) linear (mixed-effects) regression
models in 'Julia' using familiar model fitting syntax from R. Offers
'broom'-style data frame summary functionalities for 'Julia' regression
models.

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
