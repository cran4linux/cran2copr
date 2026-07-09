%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimplexRegression
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Simplex Regression Models with Parametric or Fixed Mean Link Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-sandwich 

%description
Fits and analyzes simplex regression models with either fixed or
parametric mean link functions. Implements the simplex probability density
function, cumulative distribution function, quantile function, random
number generation, and variance evaluation. Offers several fixed and
parametric link functions for the mean submodel, tools for residual
analysis and diagnostic plotting, hypothesis testing procedures, and
influence measures such as Cook's distance and leverage (hat values).
Includes the Scout Score (SS) criterion for model selection, enabling
comprehensive inference and diagnostic analysis within the simplex
regression framework. For more details see Barndorff-Nielsen and Jorgensen
(1991) <doi:10.1016/0047-259X(91)90008-P> and Justino and Cribari-Neto
(2026) <doi:10.1016/j.apm.2025.116713>.

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
