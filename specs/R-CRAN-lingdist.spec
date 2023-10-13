%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lingdist
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Linguistic Distance and Alignment Computation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp >= 1.0.10

%description
A fast generalized edit distance and string alignment computation mainly
for linguistic aims. As a generalization to the classic edit distance
algorithms, the package allows users to define custom cost for every
symbol's insertion, deletion, and substitution. The package also allows
character combinations in any length to be seen as a single symbol which
is very useful for International Phonetic Alphabet (IPA) transcriptions
with diacritics. In addition to edit distance result, users can get
detailed alignment information such as all possible alignment scenarios
between two strings which is useful for testing, illustration or any
further usage. Either the distance matrix or its long table form can be
obtained and tools to do such conversions are provided. All functions in
the package are implemented in 'C++' and the distance matrix computation
is parallelized leveraging the 'RcppThread' package.

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
