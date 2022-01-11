%global __brp_check_rpaths %{nil}
%global packname  RCPA3
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data and Functions for R Companion to Political Analysis 3rd Ed

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-descr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-weights 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-descr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lmtest 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-utils 
Requires:         R-CRAN-weights 

%description
Bundles the datasets and functions featured in Philip H. Pollock and Barry
C. Edwards (Forthcoming 2022)<https://edge.sagepub.com/pollock>, "An R
Companion to Political Analysis, 3rd Edition," Thousand Oaks, CA: Sage
Publications.

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
