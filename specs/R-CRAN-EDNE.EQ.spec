%global packname  EDNE.EQ
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implements the EDNE-Test for Equivalence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Package implements the EDNE-test for equivalence according to Hoffelder et
al. (2015) <DOI:10.1080/10543406.2014.920344>. "EDNE" abbreviates
"Euclidean Distance between the Non-standardized Expected values". The
EDNE-test for equivalence is a multivariate two-sample equivalence test.
Distance measure of the test is the Euclidean distance. The test is an
asymptotically valid test for the family of distributions fulfilling the
assumptions of the multivariate central limit theorem (see Hoffelder et
al.,2015). The function EDNE.EQ() implements the EDNE-test for equivalence
according to Hoffelder et al. (2015). The function
EDNE.EQ.dissolution.profiles() implements a variant of the EDNE-test for
equivalence analyses of dissolution profiles (see Suarez-Sharp et al.,2020
<DOI:10.1208/s12248-020-00458-9>). EDNE.EQ.dissolution.profiles() checks
whether the quadratic mean of the differences of the expected values of
both dissolution profile populations is statistically significantly
smaller than 10 [% of label claim]. The current regulatory standard
approach for equivalence analyses of dissolution profiles is the
similarity factor f2. The statistical hypotheses underlying
EDNE.EQ.dissolution.profiles() coincide with the hypotheses for f2 (see
Hoffelder et al.,2015, Suarez-Sharp et al., 2020).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
