%global __brp_check_rpaths %{nil}
%global packname  salbm
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis for Binary Missing Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForestSRC 
Requires:         R-CRAN-randomForestSRC 

%description
In a clinical trial with repeated measures designs, outcomes are often
taken from subjects at fixed time-points.  The focus of the trial may be
to compare the mean outcome in two or more groups at some pre-specified
time after enrollment. In the presence of missing data auxiliary
assumptions are necessary to perform such comparisons.  One commonly
employed assumption is the missing at random assumption (MAR). The 'salbm'
package allows the user to perform a (parameterized) sensitivity analysis
of this assumption where the outcome of interest is binary (coded as 0, 1,
or NA).  In particular it can be used to examine the sensitivity of tests
in the difference in outcomes to violations of the MAR assumption. See the
paper Daniel O. Scharfstein, Jaron J. R. Lee, Aidan McDermott, Aimee
Campbell, Edward Nunes, Abigail G. Matthews, Ilya Shpitser
"Markov-Restricted Analysis of Randomized Trials with Non-Monotone Missing
Binary Outcomes: Sensitivity Analysis and Identification Results" (2021)
<arXiv:2105.08868>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
