%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quicR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          RT-QuIC Data Formatting and Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-slider 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-slider 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Designed for the curation and analysis of data generated from real-time
quaking-induced conversion (RT-QuIC) assays first described by Atarashi et
al. (2011) <doi:10.1038/nm.2294>. 'quicR' calculates useful metrics such
as maxpoint ratio: Rowden et al. (2023) <doi:10.1099/vir.0.069906-0>;
time-to-threshold: Shi et al. (2013) <doi:10.1186/2051-5960-1-44>; and
maximum slope. Integration with the output from plate readers allows for
seamless input of raw data into the R environment.

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
