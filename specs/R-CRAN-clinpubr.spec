%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clinpubr
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Publication

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-forestploter 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-forestploter 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-tidyr 

%description
Accelerate the process from clinical data to medical publication,
including clinical data cleaning, significant result screening, and the
generation of publish-ready tables and figures.

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
