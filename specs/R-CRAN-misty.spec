%global __brp_check_rpaths %{nil}
%global packname  misty
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions 'T. Yanagida'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-norm 
BuildRequires:    R-CRAN-r2mlm 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-norm 
Requires:         R-CRAN-r2mlm 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-writexl 

%description
Miscellaneous functions for descriptive statistics (e.g., frequency table,
cross tabulation, multilevel descriptive statistics, multilevel R-squared
measures, within-group and between-group correlation matrix, various
effect size measures), data management (e.g., grand-mean and group-mean
centering, recode variables and reverse code items, scale and group
scores, reading and writing SPSS and Excel files), missing data (e.g.,
descriptive statistics for missing data, missing data pattern, Little's
test of Missing Completely at Random, and auxiliary variable analysis),
item analysis (e.g., coefficient alpha and omega, confirmatory factor
analysis), and statistical analysis (e.g., confidence intervals,
collinearity diagnostics, analysis of variance, Levene's test, t-test,
z-test, sample size determination).

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
