%global __brp_check_rpaths %{nil}
%global packname  mlfit
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Iterative Proportional Fitting Algorithms for Nested Structures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-kimisc 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wrswoR 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-kimisc 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-wrswoR 
Requires:         R-CRAN-lifecycle 

%description
The Iterative Proportional Fitting (IPF) algorithm operates on count data.
This package offers implementations for several algorithms that extend
this to nested structures: 'parent' and 'child' items for both of which
constraints can be provided. The fitting algorithms include Iterative
Proportional Updating <https://trid.trb.org/view/881554>, Hierarchical IPF
<doi:10.3929/ethz-a-006620748>, Entropy Optimization
<https://trid.trb.org/view/881144>, and Generalized Raking
<doi:10.2307/2290793>. Additionally, a number of replication methods is
also provided such as 'Truncate, replicate, sample'
<doi:10.1016/j.compenvurbsys.2013.03.004>.

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
