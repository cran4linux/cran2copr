%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forensIT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Information Theory Tools for Forensic Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mispitools 
BuildRequires:    R-CRAN-forrel 
BuildRequires:    R-CRAN-pedprobr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-fbnet 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-pedtools 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-paramlink 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mispitools 
Requires:         R-CRAN-forrel 
Requires:         R-CRAN-pedprobr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-fbnet 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-pedtools 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-paramlink 

%description
The 'forensIT' package is a comprehensive statistical toolkit tailored for
handling missing person cases. By leveraging information theory metrics,
it enables accurate assessment of kinship, particularly when limited
genetic evidence is available. With a focus on optimizing statistical
power, 'forensIT' empowers investigators to effectively prioritize family
members, enhancing the reliability and efficiency of missing person
investigations.

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
