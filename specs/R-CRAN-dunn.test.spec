%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dunn.test
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Dunn's Test of Multiple Comparisons Using Rank Sums

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computes Dunn's test (1964) for stochastic dominance and reports the
results among multiple pairwise comparisons after a Kruskal-Wallis test
for 0th-order stochastic dominance among k groups (Kruskal and Wallis,
1952). 'dunn.test' makes k(k-1)/2 multiple pairwise comparisons based on
Dunn's z-test-statistic approximations to the actual rank statistics. The
null hypothesis for each pairwise comparison is that the probability of
observing a randomly selected value from the first group that is larger
than a randomly selected value from the second group equals one half; this
null hypothesis corresponds to that of the Wilcoxon-Mann-Whitney rank-sum
test. Like the rank-sum test, if the data can be assumed to be continuous,
and the distributions are assumed identical except for a difference in
location, Dunn's test may be understood as a test for median difference
and for mean difference. 'dunn.test' accounts for tied ranks.

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
