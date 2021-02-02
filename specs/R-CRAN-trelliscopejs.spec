%global packname  trelliscopejs
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interactive Trelliscope Displays

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-DistributionUtils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-autocogs 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-grid 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-DistributionUtils 
Requires:         R-grDevices 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-graphics 
Requires:         R-CRAN-progress 
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-autocogs 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 

%description
Trelliscope is a scalable, flexible, interactive approach to visualizing
data (Hafen, 2013 <doi:10.1109/LDAV.2013.6675164>). This package provides
methods that make it easy to create a Trelliscope display specification
for TrelliscopeJS. High-level functions are provided for creating displays
from within 'tidyverse' or 'ggplot2' workflows. Low-level functions are
also provided for creating new interfaces.

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
