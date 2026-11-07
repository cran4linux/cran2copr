%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scaledescr
%global packver   0.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Descriptive, Reliability, and Inferential Tables for Psychometric Scales and Demographic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-performance 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-openxlsx 
Requires:         R-utils 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-performance 

%description
Wraps and formats outputs from established statistical and psychometric
functions into compact tables and summaries designed for straightforward
export to CSV, Word, and Excel formats. Core utilities support
psychometric scale preparation, reliability assessment, factorability
checks, structural equation and mediation analyses, inferential tests, and
demographic summaries. The package does not introduce new statistical
methods or estimation procedures; instead, it serves as a reporting
wrapper around packages such as 'psych', 'stats', 'lavaan', and
'gtsummary' to facilitate everyday data export workflows in clinical and
psychological research. It is intended to lower the barrier to entry for
researchers transitioning into the R ecosystem, with function names
structured to be intuitive and self-descriptive.

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
