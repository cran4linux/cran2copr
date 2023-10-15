%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mkin
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Kinetic Evaluation of Chemical Degradation Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-saemix >= 3.2
BuildRequires:    R-CRAN-nlme >= 3.1.151
BuildRequires:    R-CRAN-deSolve >= 1.35
BuildRequires:    R-CRAN-inline >= 0.3.19
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-saemix >= 3.2
Requires:         R-CRAN-nlme >= 3.1.151
Requires:         R-CRAN-deSolve >= 1.35
Requires:         R-CRAN-inline >= 0.3.19
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 

%description
Calculation routines based on the FOCUS Kinetics Report (2006, 2014).
Includes a function for conveniently defining differential equation
models, model solution based on eigenvalues if possible or using numerical
solvers.  If a C compiler (on windows: 'Rtools') is installed,
differential equation models are solved using automatically generated C
functions. Heteroscedasticity can be taken into account using variance by
variable or two-component error models as described by Ranke and Meinecke
(2018) <doi:10.3390/environments6120124>.  Hierarchical degradation models
can be fitted using nonlinear mixed-effects model packages as a back end
as described by Ranke et al. (2021) <doi:10.3390/environments8080071>.
Please note that no warranty is implied for correctness of results or
fitness for a particular purpose.

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
