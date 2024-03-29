%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rtrack
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Navigation Strategy Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-crayon 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-KernSmooth 
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-terra 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-zip 

%description
A toolkit for the analysis of paths from spatial tracking experiments and
calculation of goal-finding strategies. This package is centered on an
approach using machine learning for path classification.

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
