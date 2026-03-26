%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  effectcheck
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Consistency Checker for Published Research Results

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-logger 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
A conservative, assumption-aware statistical consistency checker for
published research results. Parses test statistics, effect sizes, and
confidence intervals from text, PDF, HTML, and Word documents across
multiple citation styles including American Psychological Association
(APA), Harvard, Frontiers, PLOS ONE, Scientific Reports, Nature Human
Behaviour, PeerJ, eLife, PNAS, and others. Recomputes effect sizes using
all plausible variants when design is ambiguous, and validates internal
consistency. Supports t-tests, F-tests/ANOVA, correlations, chi-square,
z-tests, regression, and nonparametric tests. Provides
'statcheck'-compatible API functions for batch processing of files and
directories. Explicitly tracks all assumptions and uncertainty in output.
Detects decision errors (significance reversals) similar to 'statcheck'.
Note: this package is under active development and results should be
independently verified. Use is at the sole responsibility of the user.
Contributions and verification reports are welcome.

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
