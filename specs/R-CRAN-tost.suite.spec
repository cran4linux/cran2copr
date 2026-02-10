%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tost.suite
%global packver   3.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Two One-Sided Tests for Equivalence

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-index0 
BuildRequires:    R-CRAN-lm.beta 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-webuse 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-index0 
Requires:         R-CRAN-lm.beta 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-webuse 

%description
Ports the 'Stata' ado package 'tost' which provides a suite of commands to
perform two one-sided tests for equivalence following the approach by
Schuirman (1987) <doi:10.1007/BF01068419>. Commands are provided for t
tests on means, z tests on proportions, McNemar's test (1947)
<doi:10.1007/BF02295996> on proportions and related tests, tests on the
regression coefficients from OLS linear regression (not yet implementing
all of the current regression options from the 'Stata' 'tostregress'
command, e.g., survey regression options, estimation options, etc.),
Wilcoxon's (1945) <doi:10.2307/3001968> signed rank tests,
Wilcoxon-Mann-Whitney (1947) <doi:10.1214/aoms/1177730491> rank sum tests,
supporting inference about equivalence for a number of paired and
unpaired, parametric and nonparametric study designs and data types. Each
command tests a null hypothesis that samples were drawn from populations
different by at least plus or minus some researcher-defined level of
tolerance, which can be defined in terms of units of the data or rank
units (Delta), or in units of the test statistic's distribution (epsilon)
except for tost.rrp() and tost.rrpi().  Enough evidence rejects this null
hypothesis in favor of equivalence within the tolerance.  Equivalence
intervals for all tests may be defined symmetrically or asymmetrically.

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
