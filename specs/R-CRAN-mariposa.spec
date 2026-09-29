%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mariposa
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          'SPSS'-Compatible Statistical Tools for Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-stats 
Requires:         R-utils 

%description
Statistical analysis of survey data with full support for survey weights,
grouped operations, and 'tidyverse' integration. Provides 80 functions for
data import/export ('SPSS', 'Stata', 'SAS', 'Excel') with label
roundtripping and tagged NA preservation, label management (variable
labels, value labels, type conversions, missing value declaration), data
transformation (recoding, dummy coding, standardization, centering),
descriptive statistics, codebook generation, hypothesis testing,
correlation analysis, post-hoc comparisons, weighted statistics, scale
analysis, regression, non-parametric tests, exact tests, factorial ANOVA,
and ANCOVA. Every analysis offers compact print() and detailed summary()
output with toggleable sections. Statistical results are validated against
'SPSS' version 29 within documented per-tier tolerances (see the
compatibility vignette for per-function status). Methods follow the
published algorithms of IBM Corp. (2023, "IBM SPSS Statistics
Algorithms"), the Lilliefors-corrected normality test of Dallal and
Wilkinson (1986) <doi:10.1080/00031305.1986.10475419>, and the adjusted
standardized residuals of Haberman (1973) <doi:10.2307/2529686>. Designed
for survey researchers, social scientists, and students working with
complex survey designs.

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
