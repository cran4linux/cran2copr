%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eCerto
%global packver   0.5.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.14
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tests for the Production of Reference Materials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-markdown >= 1.5
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-tidyxl 
Requires:         R-CRAN-markdown >= 1.5
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-config 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-tidyxl 

%description
The production of certified reference materials (CRMs) requires various
statistical tests depending on the task and recorded data to ensure that
reported values of CRMs are appropriate. Often these tests are performed
according to the procedures described in 'ISO GUIDE 35:2017'. The 'eCerto'
package contains a 'Shiny' app which provides functionality to load,
process, report and backup data recorded during CRM production and
facilitates following the recommended procedures. It is described in Lisec
et al (2023) <doi:10.1007/s00216-023-05099-3> and can also be accessed
online <https://apps.bam.de/shn00/eCerto/> without package installation.

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
