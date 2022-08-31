%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SEMsens
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for Sensitivity Analysis in Structural Equation Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-stats 
Requires:         R-CRAN-lavaan 
Requires:         R-stats 

%description
Perform sensitivity analysis in structural equation modeling using
meta-heuristic optimization methods (e.g., ant colony optimization and
others). The references for the proposed methods are: (1) Leite, W., &
Shen, Z., Marcoulides, K., Fish, C., & Harring, J. (2022).
<doi:10.1080/10705511.2021.1881786> (2) Harring, J. R., McNeish, D. M., &
Hancock, G. R. (2017) <doi:10.1080/10705511.2018.1506925>; (3) Fisk, C.,
Harring, J., Shen, Z., Leite, W., Suen, K., & Marcoulides, K. (2022).
<doi:10.1177/00131644211073121>; (4) Socha, K., & Dorigo, M. (2008)
<doi:10.1016/j.ejor.2006.06.046>. We also thank Dr. Krzysztof Socha for
sharing his research on ant colony optimization algorithm with continuous
domains and associated R code, which provided the base for the development
of this package.

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
