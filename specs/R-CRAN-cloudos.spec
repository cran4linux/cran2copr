%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cloudos
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Client Library for CloudOS

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 

%description
The 'CloudOS' client library for R makes it easy to interact with CloudOS
in the R environment for analysis.

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
