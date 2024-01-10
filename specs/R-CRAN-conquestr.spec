%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  conquestr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package to Extend 'ACER ConQuest'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
Extends 'ACER ConQuest' through a family of functions designed to improve
graphical outputs and help with advanced analysis (e.g., differential item
functioning).  Allows R users to call 'ACER ConQuest' from within R and
read 'ACER ConQuest' System Files (generated by the command `put`
<https://conquestmanual.acer.org/s4-00.html#put>). Requires 'ACER
ConQuest' version 5.33.2 or later. A demonstration version can be
downloaded from <https://shop.acer.org/acer-conquest-5.html>.

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
