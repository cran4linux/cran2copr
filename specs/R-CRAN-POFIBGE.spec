%global __brp_check_rpaths %{nil}
%global packname  POFIBGE
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Downloading, Reading and Analysing POF Microdata

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-projmgr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-projmgr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-RCurl 
Requires:         R-utils 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tibble 

%description
Provides tools for downloading, reading and analysing the POF, a household
survey from Brazilian Institute of Geography and Statistics - IBGE. The
data must be downloaded from the official website
<https://www.ibge.gov.br/>. Further analysis must be made using package
'survey'.

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
