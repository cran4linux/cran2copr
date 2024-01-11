%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vivainsights
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze and Visualize Data from 'Microsoft Viva Insights'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-wpa 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-ggwordcloud 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-wpa 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-ggwordcloud 
Requires:         R-CRAN-lifecycle 

%description
Provides a versatile range of functions, including exploratory data
analysis, time-series analysis, organizational network analysis, and data
validation, whilst at the same time implements a set of best practices in
analyzing and visualizing data specific to 'Microsoft Viva Insights'.

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
