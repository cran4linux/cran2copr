%global packname  fishualize
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Color Palettes Based on Fish Species

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-png 
Requires:         R-CRAN-downloader 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-curl 

%description
Implementation of color palettes based on fish species.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
