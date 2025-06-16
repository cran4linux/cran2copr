%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tergm
%global packver   4.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate and Diagnose Models for Network Evolution Based on Exponential-Family Random Graph Models

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ergm >= 4.9.0
BuildRequires:    R-CRAN-statnet.common >= 4.12.0
BuildRequires:    R-CRAN-network >= 1.19.0
BuildRequires:    R-CRAN-purrr >= 1.0.4
BuildRequires:    R-CRAN-robustbase >= 0.99.4.1
BuildRequires:    R-CRAN-ergm.multi >= 0.3.0
BuildRequires:    R-CRAN-coda >= 0.19.4.1
BuildRequires:    R-CRAN-networkDynamic >= 0.11.5
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-ergm >= 4.9.0
Requires:         R-CRAN-statnet.common >= 4.12.0
Requires:         R-CRAN-network >= 1.19.0
Requires:         R-CRAN-purrr >= 1.0.4
Requires:         R-CRAN-robustbase >= 0.99.4.1
Requires:         R-CRAN-ergm.multi >= 0.3.0
Requires:         R-CRAN-coda >= 0.19.4.1
Requires:         R-CRAN-networkDynamic >= 0.11.5
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-MASS 

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
