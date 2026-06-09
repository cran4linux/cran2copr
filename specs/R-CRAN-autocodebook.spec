%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autocodebook
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Codebook and Tracking for 'Spark' and 'dplyr' Pipelines

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-grid 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-gt 
Requires:         R-grid 

%description
Wraps 'dplyr' verbs (mutate, summarise, filter) to automatically capture
variable metadata (type, source columns, categories, and source code),
producing a codebook and eligibility tracking table with zero manual
documentation. Works with both 'sparklyr' (tbl_spark) and local data
frames. Adds big-data optimizations (caching, assume-unique counting,
checkpointing) and a standardized report module with an eligibility
flowchart, editable codebook export (HTML, DOCX, XLSX), and
cross-sectional or longitudinal variable inspection. The eligibility
flowchart follows the CONSORT statement (Schulz, Altman and Moher (2010)
<doi:10.1136/bmj.c332>) and the reporting of observational cohort studies
follows the STROBE recommendations (von Elm and others (2007)
<doi:10.1371/journal.pmed.0040296>).

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
