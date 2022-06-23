%global __brp_check_rpaths %{nil}
%global packname  tergm
%global packver   4.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Models for Network Evolution Based on Exponential-Family Random Graph Models

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-statnet.common >= 4.4.0
BuildRequires:    R-CRAN-ergm >= 4.2.2
BuildRequires:    R-CRAN-nlme >= 3.1.139
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-robustbase >= 0.93.5
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-networkDynamic >= 0.10.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-MASS >= 7.3.51.4
Requires:         R-CRAN-statnet.common >= 4.4.0
Requires:         R-CRAN-ergm >= 4.2.2
Requires:         R-CRAN-nlme >= 3.1.139
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-robustbase >= 0.93.5
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-networkDynamic >= 0.10.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-purrr 

%description
An integrated set of extensions to the 'ergm' package to analyze and
simulate network evolution based on exponential-family random graph models
(ERGM). 'tergm' is a part of the 'statnet' suite of packages for network
analysis. See Krivitsky and Handcock (2014) <doi:10.1111/rssb.12014> and
Carnegie, Krivitsky, Hunter, and Goodreau (2015)
<doi:10.1080/10618600.2014.903087>.

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
