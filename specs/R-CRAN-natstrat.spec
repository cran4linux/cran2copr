%global __brp_check_rpaths %{nil}
%global packname  natstrat
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Obtain Unweighted Natural Strata that Balance Many Covariates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-pps 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ramify 
BuildRequires:    R-CRAN-slam 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-Rglpk 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-pps 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ramify 
Requires:         R-CRAN-slam 

%description
Natural strata can be used in observational studies to balance the
distributions of many covariates across any number of treatment groups and
any number of comparisons. These strata have proportional amounts of units
within each stratum across the treatments, allowing for simple
interpretation and aggregation across strata. Within each stratum, the
units are chosen using randomized rounding of a linear program that
balances many covariates. To solve the linear program, the 'Gurobi'
commercial optimization software is recommended, but not required. The
'gurobi' R package can be installed following the instructions at
<https://www.gurobi.com/documentation/9.1/refman/ins_the_r_package.html>.

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
