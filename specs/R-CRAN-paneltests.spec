%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  paneltests
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Panel Data Pre-Testing and Diagnostic Suite

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Pre-testing and diagnostic tools for panel data analysis. Researchers
should run these tests before any panel regression to verify modelling
assumptions. The package implements: (1) the Hsiao (2014,
<ISBN:978-1-107-65763-2>) homogeneity F-tests (F1/F2/F3), Swamy (1970)
<doi:10.2307/1913012> parameter heterogeneity test, and Pesaran (2004)
<doi:10.2139/ssrn.572504> cross-sectional dependence test via xtpretest();
(2) missing-data detection, mechanism testing, and imputation for
unbalanced panels via xtmispanel(); (3) quantile-regression
cross-sectional dependence tests (T_tau and T-tilde_tau statistics) of
Demetrescu, Hosseinkouchack and Rodrigues (2023)
<doi:10.1016/j.jeconom.2022.09.001> via xtcsdq(); and (4) the panel
quantile-regression slope homogeneity S-hat and D-hat statistics of
Galvao, Juhl, Montes-Rojas and Olmo (2017)
<doi:10.1080/07350015.2015.1054493> via xtqsh(). Together these tests
address three fundamental pre-testing questions: (i) are slopes
homogeneous? (ii) is there cross-sectional dependence? and (iii) is the
panel balanced and is missingness ignorable?

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
