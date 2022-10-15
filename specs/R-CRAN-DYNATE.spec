%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DYNATE
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Aggregation Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 

%description
A multiple testing procedure aims to find the rare-variant association
regions. When variants are rare, the single variant association test
approach suffers from low power. To improve testing power, the procedure
dynamically and hierarchically aggregates smaller genome regions to larger
ones and performs multiple testing for disease associations with a
controlled node-level false discovery rate. This method are members of the
family of ancillary information assisted recursive testing introduced in
Pura, Li, Chan and Xie (2021) <arXiv:1906.07757v2> and Li, Sung and Xie
(2021) <arXiv:2103.11085v2>.

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
