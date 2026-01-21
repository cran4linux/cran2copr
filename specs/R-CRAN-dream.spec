%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dream
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Relational Event Analysis and Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-fastmatch 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-fastmatch 

%description
A set of tools for relational and event analysis, including two- and
one-mode network brokerage and structural measures, and helper functions
optimized for relational event analysis with large datasets, including
creating relational risk sets, computing network statistics, estimating
relational event models, and simulating relational event sequences. For
more information on relational event models, see Butts (2008)
<doi:10.1111/j.1467-9531.2008.00203.x>, Lerner and Lomi (2020)
<doi:10.1017/nws.2019.57>, Bianchi et al. (2024)
<doi:10.1146/annurev-statistics-040722-060248>, and Butts et al. (2023)
<doi:10.1017/nws.2023.9>. In terms of the structural measures in this
package, see Leal (2025) <doi:10.1177/00491241251322517>, Burchard and
Cornwell (2018) <doi:10.1016/j.socnet.2018.04.001>, and Fujimoto et al.
(2018) <doi:10.1017/nws.2018.11>. This package was developed with support
from the National Science Foundation’s (NSF) Human Networks and Data
Science Program (HNDS) under award number 2241536 (PI: Diego F. Leal). Any
opinions, findings, and conclusions, or recommendations expressed in this
material are those of the authors and do not necessarily reflect the views
of the NSF.

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
