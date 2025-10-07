%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NIMAA
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nominal Data Mining Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-skimr 
BuildRequires:    R-CRAN-bnstruct 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-missMDA 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-softImpute 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-stats 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-bipartite 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-skimr 
Requires:         R-CRAN-bnstruct 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-missMDA 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-softImpute 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-visNetwork 
Requires:         R-stats 

%description
Functions for nominal data mining based on bipartite graphs, which build a
pipeline for analysis and missing values imputation. Methods are mainly
from the paper: Jafari, Mohieddin, et al. (2021)
<doi:10.1101/2021.03.18.436040>, some new ones are also included.

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
