%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  actxps
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Actuarial Experience Studies: Prepare Data, Summarize Results, and Create Reports

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vctrs 

%description
Experience studies are used by actuaries to explore historical experience
across blocks of business and to inform assumption setting activities.
This package provides functions for preparing data, creating studies, and
beginning assumption development. Experience study methods, including
exposure calculations, are described in: Atkinson & McGarry (2016)
"Experience Study Calculations"
<https://www.soa.org/49378a/globalassets/assets/files/research/experience-study-calculations.pdf>.
The limited fluctuation credibility method used by the 'exp_stats()'
function is described in: Herzog (1999, ISBN:1-56698-374-6) "Introduction
to Credibility Theory".

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
