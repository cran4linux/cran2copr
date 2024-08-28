%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  longpower
%global packver   1.0.26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.26
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size Calculations for Longitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-methods 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-CRAN-nlme 
Requires:         R-methods 

%description
Compute power and sample size for linear models of longitudinal data.
Supported models include mixed-effects models and models fit by
generalized least squares and generalized estimating equations. The
package is described in Iddi and Donohue (2022)
<DOI:10.32614/RJ-2022-022>. Relevant formulas are derived by Liu and Liang
(1997) <DOI:10.2307/2533554>, Diggle et al (2002) <ISBN:9780199676750>,
and Lu, Luo, and Chen (2008) <DOI:10.2202/1557-4679.1098>.

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
