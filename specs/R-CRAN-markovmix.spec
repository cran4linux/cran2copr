%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  markovmix
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture of Markov Chains with Support of Higher Orders and Multiple Sequences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-pillar >= 1.9.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-pillar >= 1.9.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-Rcpp 

%description
Fit mixture of Markov chains of higher orders from multiple sequences. It
is also compatible with ordinary 1-component, 1-order or single-sequence
Markov chains. Various utility functions are provided to derive transition
patterns, transition probabilities per component and component priors. In
addition, print(), predict() and component extracting/replacing methods
are also defined as a convention of mixture models.

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
