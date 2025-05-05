%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PerMallows
%global packver   1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15
Release:          1%{?dist}%{?buildtag}
Summary:          Permutations and Mallows Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-utils 

%description
Includes functions to work with the Mallows and Generalized Mallows
Models. The considered distances are Kendall's-tau, Cayley, Hamming and
Ulam and it includes functions for making inference, sampling and learning
such distributions, some of which are novel in the literature. As a
by-product, PerMallows also includes operations for permutations, paying
special attention to those related with the Kendall's-tau, Cayley, Ulam
and Hamming distances. It is also possible to generate random permutations
at a given distance, or with a given number of inversions, or cycles, or
fixed points or even with a given length on LIS (longest increasing
subsequence).

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
