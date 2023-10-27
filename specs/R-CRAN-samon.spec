%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  samon
%global packver   4.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis for Missing Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
In a clinical trial with repeated measures designs, outcomes are often
taken from subjects at fixed time-points.  The focus of the trial may be
to compare the mean outcome in two or more groups at some pre-specified
time after enrollment. In the presence of missing data auxiliary
assumptions are necessary to perform such comparisons.  One commonly
employed assumption is the missing at random assumption (MAR).  The
'samon' package allows the user to perform a (parameterized) sensitivity
analysis of this assumption.  In particular it can be used to examine the
sensitivity of tests in the difference in outcomes to violations of the
MAR assumption.  The sensitivity analysis can be performed under two
scenarios, a) where the data exhibit a monotone missing data pattern (see
the samon() function), and, b) where in addition to a monotone missing
data pattern the data exhibit intermittent missing values (see the
samonIM() function).

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
