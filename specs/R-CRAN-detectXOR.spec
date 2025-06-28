%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  detectXOR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          XOR Pattern Detection and Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-DescTools >= 0.99.50
BuildRequires:    R-CRAN-ggh4x >= 0.2.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-DescTools >= 0.99.50
Requires:         R-CRAN-ggh4x >= 0.2.3
Requires:         R-stats 
Requires:         R-CRAN-ggthemes 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-base64enc 

%description
Provides tools for detecting XOR-like patterns in variable pairs in
two-class data sets. Includes visualizations for pattern exploration and
reporting capabilities with both text and HTML output formats.

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
