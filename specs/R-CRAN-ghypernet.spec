%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ghypernet
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fit and Simulate Generalised Hypergeometric Ensembles of Graphs

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-methods 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-texreg 
Requires:         R-methods 

%description
Provides functions for model fitting and selection of generalised
hypergeometric ensembles of random graphs (gHypEG). To learn how to use
it, check the vignettes for a quick tutorial. Please reference its use as
Casiraghi, G., Nanumyan, V. (2019) <doi:10.5281/zenodo.2555300> together
with those relevant references from the one listed below. The package is
based on the research developed at the Chair of Systems Design, ETH
Zurich. Casiraghi, G., Nanumyan, V., Scholtes, I., Schweitzer, F. (2016)
<doi:10.48550/arXiv.1607.02441>. Casiraghi, G., Nanumyan, V., Scholtes,
I., Schweitzer, F. (2017) <doi:10.1007/978-3-319-67256-4_11>. Casiraghi,
G., (2017) <doi:10.48550/arXiv.1702.02048>. Brandenberger, L., Casiraghi,
G., Nanumyan, V., Schweitzer, F. (2019) <doi:10.1145/3341161.3342926>.
Casiraghi, G. (2019) <doi:10.1007/s41109-019-0241-1>. Casiraghi, G.,
Nanumyan, V. (2021) <doi:10.1038/s41598-021-92519-y>. Casiraghi, G. (2021)
<doi:10.1088/2632-072X/ac0493>.

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
