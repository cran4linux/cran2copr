%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICCDesign
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intraclass Correlation Coefficient (ICC) Design, Calculation and Interactive 'shiny' Toolkit

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-shiny 

%description
A comprehensive toolkit for intraclass correlation coefficient (ICC)
analysis, integrating three core functionalities: (1) Closed-form sample
size calculation for ICC estimation with assurance probability, based on
Zou (2012) <doi:10.1002/sim.5466>; (2) Full implementation of all 10 ICC
types (6 common + 4 supplementary) for point estimation, exact confidence
interval calculation, and formal hypothesis testing, following the methods
of McGraw & Wong (1996) <doi:10.1037/1082-989X.1.1.30> and the standard
decision framework; (3) An interactive 'shiny' application that guides
users through ICC type selection, performs calculations, and provides
reliability evaluation based on the Koo & Li (2016)
<doi:10.1016/j.jcm.2016.02.012> criteria. Compared to existing packages,
it provides a unified decision workflow and supports all less common ICC
variants.

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
