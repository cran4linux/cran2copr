%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rcope
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Cope with Endogeneity Problems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-car 

%description
Researchers across disciplines often face biased regression model
estimates due to endogenous regressors correlated with the error term.
Traditional solutions require instrumental variables (IVs), which are
often difficult to find and validate. This package provides flexible,
alternative IV-free methods using copulas, as described in the practical
guide to endogeneity correction using copulas (Yi Qian, Tony Koschmann,
and Hui Xie 2025) <doi:10.1177/00222429251410844>. The current version
implements the two-stage copula endogeneity correction (2sCOPE) method to
fit models with continuous endogenous regressors and both continuous and
discrete exogenous regressors, as described in Fan Yang, Yi Qian, and Hui
Xie (2024) <doi:10.1177/00222437241296453>. Using this method, users can
address regressor endogeneity problems in nonexperimental data without
requiring IVs.

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
