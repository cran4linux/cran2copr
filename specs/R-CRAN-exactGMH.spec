%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exactGMH
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exact and Permutation-Based Mantel Tests for Differential Item Functioning in Dichotomous and Polytomous Items

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Screens dichotomous and polytomous test items for Differential Item
Functioning (DIF) using an extension of the Mantel (1963)
<doi:10.1080/01621459.1963.10500879> and generalized Mantel-Haenszel
statistic, with statistical significance computed via permutation rather
than the conventional asymptotic chi-square approximation. Following
Hemerik and Goeman (2018) <doi:10.1007/s11749-017-0571-1>, the permutation
p-value is exact at the nominal level rather than an approximation, even
for a finite number of permutations. This makes the test valid for small
samples (fewer than 200 examinees per group), a condition common in
classroom-, program-, and institution-level assessment where existing
exact-inference options in other software are restricted to dichotomous
items only. An optional Benjamini-Hochberg or Bonferroni correction
addresses multiple comparisons when screening many items at once.

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
