%global __brp_check_rpaths %{nil}
%global packname  rmcfs
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          The MCFS-ID Algorithm for Feature Selection and Interdependency Discovery

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.70
Requires:         R-core >= 2.70
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.0.1
BuildRequires:    R-CRAN-rJava >= 0.5.0
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-data.table >= 1.0.1
Requires:         R-CRAN-rJava >= 0.5.0
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-igraph 

%description
MCFS-ID (Monte Carlo Feature Selection and Interdependency Discovery) is a
Monte Carlo method-based tool for feature selection. It also allows for
the discovery of interdependencies between the relevant features. MCFS-ID
is particularly suitable for the analysis of high-dimensional, 'small n
large p' transactional and biological data. M. Draminski, J. Koronacki
(2018) <doi:10.18637/jss.v085.i12>.

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
