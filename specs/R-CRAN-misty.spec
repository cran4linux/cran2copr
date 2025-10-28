%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  misty
%global packver   0.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.6
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions 'T. Yanagida'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-rstudioapi 

%description
Miscellaneous functions for (1) data handling (e.g., grand-mean and
group-mean centering, coding variables and reverse coding items, scale and
cluster scores, reading and writing Excel and SPSS files), (2) descriptive
statistics (e.g., frequency table, cross tabulation, effect size
measures), (3) missing data (e.g., descriptive statistics for missing
data, missing data pattern, Little's test of Missing Completely at Random,
and auxiliary variable analysis), (4) multilevel data (e.g., multilevel
descriptive statistics, within-group and between-group correlation matrix,
multilevel confirmatory factor analysis, level-specific fit indices,
cross-level measurement equivalence evaluation, multilevel composite
reliability, and multilevel R-squared measures), (5) item analysis (e.g.,
confirmatory factor analysis, coefficient alpha and omega, between-group
and longitudinal measurement equivalence evaluation), (6) statistical
analysis (e.g., bootstrap confidence intervals, collinearity and residual
diagnostics, dominance analysis, between- and within-subject analysis of
variance, latent class analysis, t-test, z-test, sample size
determination), and (7) functions to interact with 'Blimp' and 'Mplus'.

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
