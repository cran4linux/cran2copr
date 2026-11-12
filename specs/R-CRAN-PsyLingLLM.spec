%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PsyLingLLM
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Controlled Psycholinguistic Experiments with Large Language Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringi 

%description
Runs controlled psycholinguistic, psychological, cognitive, and
educational experiments with large language models. Registry-based
configuration separates models, providers, and application programming
interfaces so that compatible services can share experimental designs.
Functions support randomized and factorial trials, multi-turn
conversations, response and reasoning capture, timing and token
measurements, and structured result export. For methodological context on
using language models as experimental participants, see Dillion et al.
(2023) <doi:10.1016/j.tics.2023.04.008>.

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
