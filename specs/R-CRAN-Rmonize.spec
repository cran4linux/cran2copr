%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rmonize
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Support Retrospective Harmonization of Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-fabR >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-madshapR 
Requires:         R-CRAN-fabR >= 2.0.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-haven 
Requires:         R-utils 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-madshapR 

%description
Functions to support rigorous retrospective data harmonization processing,
evaluation, and documentation across datasets from different studies based
on Maelstrom Research guidelines. The package includes the core functions
to evaluate and format the main inputs that define the harmonization
process, apply specified processing rules to generate harmonized data,
diagnose processing errors, and summarize and evaluate harmonized outputs.
The main inputs that define the processing are a DataSchema (list and
definitions of harmonized variables to be generated) and Data Processing
Elements (processing rules to be applied to generate harmonized variables
from study-specific variables). The main outputs of processing are
harmonized datasets, associated metadata, and tabular and visual summary
reports. As described in Maelstrom Research guidelines for rigorous
retrospective data harmonization (Fortier I and al. (2017)
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
