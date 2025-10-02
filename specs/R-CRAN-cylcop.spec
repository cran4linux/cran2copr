%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cylcop
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Circular-Linear Copulas with Angular Symmetry for Movement Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-GoFKernel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-mixR 
BuildRequires:    R-CRAN-transport 
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-circular 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-GoFKernel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-movMF 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mixR 
Requires:         R-CRAN-transport 

%description
Classes (S4) of circular-linear, symmetric copulas with corresponding
methods, extending the 'copula' package. These copulas are especially
useful for modeling correlation in discrete-time movement data. Methods
for density, (conditional) distribution, random number generation,
bivariate dependence measures and fitting parameters using maximum
likelihood and other approaches. The package also contains methods for
visualizing movement data and copulas.

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
