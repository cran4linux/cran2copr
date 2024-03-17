%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DImodelsMulti
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Multivariate Diversity-Interactions Models with Repeated Measures

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DImodels 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-DImodels 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-Matrix 

%description
An add-on package to 'DImodels' for the fitting of biodiversity and
ecosystem function relationship study data with multiple ecosystem
function responses and/or time points. This package uses the multivariate
and repeated measures Diversity-Interactions (DI) methods developed by
Kirwan et al. (2009) <doi:10.1890/08-1684.1>, Finn et al. (2013)
<doi:10.1111/1365-2664.12041>, and Dooley et al. (2015)
<doi:10.1111/ele.12504>.

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
