%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  starling
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Record Linkage for Public Health Surveillance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-reclin2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-reclin2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 

%description
Record linkage for public health surveillance datasets using either the
Fellegi-Sunter probabilistic framework (via reclin2) or deterministic
exact-key matching. Provides pre-linkage data quality auditing
(preflight()), Medicare number checksum validation (check_medicare()),
blocking variable construction (flock()), and the murmuration() linkage
engine. murmuration() expresses linkage as a single cohort-to-event
concept (linking a linelist of people to a dated stream of vaccination,
hospitalisation, or case events within a before/during/after time window),
with the historical four-code taxonomy (case-to-hospitalisation,
vaccination-to-case, vaccination-to-hospitalisation, vaccination-to-event)
retained as deprecated aliases. Also provides linkage weight distribution
visualisation (murmuration_plot()) and threshold sensitivity analysis
(perch()) with annotated AIHW, WA Data Linkage Unit, and PHRN reference
benchmarks. perch() can be called standalone or triggered automatically
mid-linkage via murmuration(perch_before_linking = TRUE). Includes
synthetic datasets (cases_notifiable, vax_air) and three vignettes
demonstrating the complete linkage workflow. Part of the aviary public
health surveillance ecosystem.

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
