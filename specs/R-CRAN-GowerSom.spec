%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GowerSom
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Self-Organizing Maps for Mixed-Attribute Data Using Gower Distance

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gower 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-StatMatch 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gower 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-reshape2 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-cli 

%description
Implements a variant of the Self-Organizing Map (SOM) algorithm designed
for mixed-attribute datasets. Similarity between observations is computed
using the Gower distance, and categorical prototypes are updated via
heuristic strategies (weighted mode and multinomial sampling). Provides
functions for model fitting, mapping, visualization (U-Matrix and
component planes), and evaluation, making SOM applicable to heterogeneous
real-world data. For methodological details see Sáez and Salas (2026)
<doi:10.1007/s41060-025-00941-6>.

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
