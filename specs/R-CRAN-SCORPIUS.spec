%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCORPIUS
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Inferring Developmental Chronologies from Single-Cell RNA Sequencing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-princurve >= 2.1.4
BuildRequires:    R-CRAN-ggplot2 >= 2.0
BuildRequires:    R-CRAN-dynutils >= 1.0.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dynwrap 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lmds 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-TSP 
Requires:         R-CRAN-princurve >= 2.1.4
Requires:         R-CRAN-ggplot2 >= 2.0
Requires:         R-CRAN-dynutils >= 1.0.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dynwrap 
Requires:         R-grDevices 
Requires:         R-CRAN-lmds 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-TSP 

%description
An accurate and easy tool for performing linear trajectory inference on
single cells using single-cell RNA sequencing data. In addition,
'SCORPIUS' provides functions for discovering the most important genes
with respect to the reconstructed trajectory, as well as nice
visualisation tools. Cannoodt et al. (2016) <doi:10.1101/079509>.

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
