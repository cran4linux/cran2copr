%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sivirep
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Wrangling and Automated Reports from 'SIVIGILA' Source

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-epitrix 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-config 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-epitrix 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-CRAN-sysfonts 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-kableExtra 

%description
Data wrangling, pre-processing, and generating automated reports from
Colombia's epidemiological surveillance system, 'SIVIGILA'
<https://portalsivigila.ins.gov.co/>. It provides a customizable R
Markdown template for analysis and automatic generation of epidemiological
reports that can be adapted to local, regional, and national contexts.
This tool offers a standardized and reproducible workflow that helps to
reduce manual labor and potential errors in report generation, improving
their efficiency and consistency.

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
