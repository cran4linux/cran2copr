%global __brp_check_rpaths %{nil}
%global packname  SE.EQ
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          SE-Test for Equivalence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Implements the SE-test for equivalence according to Hoffelder et al.
(2015) <DOI:10.1080/10543406.2014.920344>. The SE-test for equivalence is
a multivariate two-sample equivalence test. Distance measure of the test
is the sum of standardized differences between the expected values or in
other words: the sum of effect sizes (SE) of all components of the two
multivariate samples. The test is an asymptotically valid test for
normally distributed data (see Hoffelder et al.,2015). The function
SE.EQ() implements the SE-test for equivalence according to Hoffelder et
al. (2015). The function SE.EQ.dissolution.profiles() implements a variant
of the SE-test for equivalence for similarity analyses of dissolution
profiles as mentioned in Suarez-Sharp et al.(2020)
<DOI:10.1208/s12248-020-00458-9>). The equivalence margin used in
SE.EQ.dissolution.profiles() is analogically defined as for the T2EQ
approach according to Hoffelder (2019) <DOI:10.1002/bimj.201700257>) by
means of a systematic shift in location of 10 [%% of label claim] of both
dissolution profile populations. SE.EQ.dissolution.profiles() checks
whether the weighted mean of the differences of the expected values of
both dissolution profile populations is statistically significantly
smaller than 10 [%% of label claim]. The weights are built up by the
inverse variances.

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
