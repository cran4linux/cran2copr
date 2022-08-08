%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qPCRtools
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for qPCR

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpmisc 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-sjmisc 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xlsx 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpmisc 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-sjmisc 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xlsx 

%description
RT-qPCR is a widely used method to detect the expression level of genes in
biological research. A crucial step in processing qPCR data is to
calculate the amplification efficiency of genes to determine which method
should be used to calculate expression level of genes. This Package can do
it easily. In addition to that, this package can calculate the expression
level of genes based on three methods.

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
