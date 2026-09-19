%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCAtools
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Direction-Aware Sufficiency Condition Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NCA >= 5.0.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-NCA >= 5.0.2
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a direction-aware interface for analysing bivariate sufficiency
statements from empty-space frontier patterns. Logical sufficiency
directions (high or low levels of a condition and outcome) are kept
separate from the physical location of the empty corner in the scatter
plot. Computation is delegated to version 5 of the 'NCA' package based on
Dul (2016) <doi:10.1177/1094428115584005>, using the contraposition
between necessity and sufficiency. Threshold tables are computed in actual
units and converted by this package, so percentage, percentile and
standard-deviation scales follow one stated reporting convention in every
sufficiency direction. Includes tidy summaries, threshold rules, plots,
random-data generation, permutation tests, and power analysis. An ordinary
least-squares line can be drawn beside the frontier as a central-tendency
reference; it is an average-effect summary and never a component of a
sufficiency claim. An empty-space pattern alone does not establish
causality or deterministic sufficiency.

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
