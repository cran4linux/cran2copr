%global packname  foqat
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Field Observation Quick Analysis Toolkit

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lmodel2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-lmodel2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-gridExtra 

%description
Tools for quickly processing and analyzing field observation data and air
quality data. This tools contain functions that facilitate analysis in
atmospheric chemistry (especially in ozone pollution). Some functions of
time series are also applicable to other fields. For detail please view
homepage<https://github.com/tianshu129/foqat>. Scientific Reference: 1.
The Hydroxyl Radical (OH) Reactivity: Roger Atkinson and Janet Arey (2003)
<doi:10.1021/cr0206420>. 2. Ozone Formation Potential (OFP):
<https://ww3.arb.ca.gov/regact/2009/mir2009/mir10.pdf>. 3. TUV model:
<https://www2.acom.ucar.edu/modeling/tropospheric-ultraviolet-and-visible-tuv-radiation-model>.

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
