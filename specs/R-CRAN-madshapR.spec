%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  madshapR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Support Technical Processes Following 'Maelstrom Research' Standards

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-fabR >= 2.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-fabR >= 2.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidytext 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-bookdown 
Requires:         R-stats 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-fs 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 

%description
Functions to support rigorous processes in data cleaning, evaluation, and
documentation across datasets from different studies based on Maelstrom
Research guidelines. The package includes the core functions to evaluate
and format the main inputs that define the process, diagnose errors, and
summarize and evaluate datasets and their associated data dictionaries.
The main outputs are clean datasets and associated metadata, and tabular
and visual summary reports. As described in Maelstrom Research guidelines
for rigorous retrospective data harmonization (Fortier I and al. (2017)
<doi:10.1093/ije/dyw075>).

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
