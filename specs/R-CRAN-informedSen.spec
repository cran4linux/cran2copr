%global __brp_check_rpaths %{nil}
%global packname  informedSen
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis Informed by a Test for Bias

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sensitivitymult 
BuildRequires:    R-stats 
Requires:         R-CRAN-sensitivitymult 
Requires:         R-stats 

%description
After testing for biased treatment assignment in an observational study
using an unaffected outcome, the sensitivity analysis is constrained to be
compatible with that test.  The package uses the optimization software
gurobi obtainable from <https://www.gurobi.com/>, together with its
associated R package, also called gurobi; see:
<https://www.gurobi.com/documentation/7.0/refman/installing_the_r_package.html>.
The method is a substantial computational and practical enhancement of a
concept introduced in Rosenbaum (1992) Detecting bias with confidence in
observational studies Biometrika, 79(2), 367-374
<doi:10.1093/biomet/79.2.367>.

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
