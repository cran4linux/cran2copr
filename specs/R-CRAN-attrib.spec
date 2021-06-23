%global __brp_check_rpaths %{nil}
%global packname  attrib
%global packver   2021.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2021.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Attributable Burden of Disease

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pbs 
BuildRequires:    R-CRAN-dlnm 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mvmeta 
BuildRequires:    R-CRAN-tsModel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pbs 
Requires:         R-CRAN-dlnm 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mvmeta 
Requires:         R-CRAN-tsModel 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-progress 

%description
Provides functions for estimating the attributable burden of disease due
to risk factors. The posterior simulation is performed using arm::sim as
described in Gelman, Hill (2012) <doi:10.1017/CBO9780511790942> and the
attributable burden method is based on Nielsen, Krause, Molbak
<doi:10.1111/irv.12564>.

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
