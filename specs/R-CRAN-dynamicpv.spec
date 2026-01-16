%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynamicpv
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluates Present Values and Health Economic Models with Dynamic Pricing and Uptake

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
The goal of 'dynamicpv' is to provide a simple way to calculate (net)
present values and outputs from health economic models (especially
cost-effectiveness and budget impact) in discrete time that reflect
dynamic pricing and dynamic uptake. Dynamic pricing is also known as life
cycle pricing; dynamic uptake is also known as multiple or stacked
cohorts, or dynamic disease prevalence. Shafrin (2024)
<doi:10.1515/fhep-2024-0014> provides an explanation of dynamic value
elements, in the context of Generalized Cost Effectiveness Analysis, and
Puls (2024) <doi:10.1016/j.jval.2024.03.006> reviews challenges of
incorporating such dynamic value elements. This package aims to reduce
those challenges.

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
