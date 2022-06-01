%global __brp_check_rpaths %{nil}
%global packname  PUPMSI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Moisture Sorption Isotherm Modeling Program

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-nls2 
Requires:         R-stats 

%description
Contains sixteen moisture sorption isotherm models, which evaluate the
fitness of adsorption and desorption curves for further understanding of
the relationship between moisture content and water activity. Fitness
evaluation is conducted through parameter estimation and error analysis.
Moreover, graphical representation, hysteresis area estimation, and
isotherm classification through the equation of Blahovec & Yanniotis
(2009) <doi:10.1016/j.jfoodeng.2008.08.007> which is based on the
classification system introduced by Brunauer et. al. (1940)
<doi:10.1021/ja01864a025> are also included for the visualization of
models and hysteresis.

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
