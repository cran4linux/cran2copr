%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FeatureHashing
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Creates a Model Matrix via Feature Hashing with a Formula Interface

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-BH >= 1.54.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-digest >= 0.6.8
BuildRequires:    R-CRAN-Rcpp >= 0.11
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-digest >= 0.6.8
Requires:         R-CRAN-Rcpp >= 0.11
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
Feature hashing, also called as the hashing trick, is a method to
transform features of a instance to a vector. Thus, it is a method to
transform a real dataset to a matrix. Without looking up the indices in an
associative array, it applies a hash function to the features and uses
their hash values as indices directly. The method of feature hashing in
this package was proposed in Weinberger et al. (2009) <arXiv:0902.2206>.
The hashing algorithm is the murmurhash3 from the 'digest' package. Please
see the README in <https://github.com/wush978/FeatureHashing> for more
information.

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
