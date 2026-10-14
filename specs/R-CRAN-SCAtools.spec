%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCAtools
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Direction-Aware Sufficient Condition Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NCA >= 5.0.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-NCA >= 5.0.2
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-quantreg 
Requires:         R-stats 
Requires:         R-utils 

%description
Tests whether a high or low level of a condition is enough to guarantee a
high or low level of an outcome. Such a claim predicts that one corner of
the condition-outcome scatter plot is empty of observations. The package
estimates the boundary of that empty corner, its size as a share of the
scope (the effect size), a permutation test against random pairing, and a
threshold table giving the condition level that guarantees each outcome
level, in actual units, percentages, percentiles or standard deviations.
Each of the four directions (high or low condition, high or low outcome)
is stated as a claim and mapped to its empty corner. Because a condition
can rule out low outcomes while barely moving the average, results can be
set beside ordinary least-squares and median regression slopes, showing
whether the data hold an average effect, a sufficiency effect or both.
Also provides plots, influential-case diagnostics, scope-sensitivity and
resampling checks, random-data generation and power analysis for planning
studies. Frontiers are estimated with the 'NCA' package.

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
