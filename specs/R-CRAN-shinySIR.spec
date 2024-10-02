%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinySIR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Plotting for Mathematical Models of Infectious Disease Spread

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-deSolve >= 1.2
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-deSolve >= 1.2
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.0.1

%description
Provides interactive plotting for mathematical models of infectious
disease spread. Users can choose from a variety of common built-in
ordinary differential equation (ODE) models (such as the SIR, SIRS, and
SIS models), or create their own. This latter flexibility allows
'shinySIR' to be applied to simple ODEs from any discipline. The package
is a useful teaching tool as students can visualize how changing different
parameters can impact model dynamics, with minimal knowledge of coding in
R. The built-in models are inspired by those featured in Keeling and
Rohani (2008) <doi:10.2307/j.ctvcm4gk0> and Bjornstad (2018)
<doi:10.1007/978-3-319-97487-3>.

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
