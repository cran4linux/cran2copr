%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppJagger
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          An R Wrapper for Jagger

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-purrr >= 1.0.0

%description
A wrapper for Jagger, a morphological analyzer proposed in Yoshinaga
(2023) <arXiv:2305.19045>. Jagger uses patterns derived from morphological
dictionaries and training data sets and applies them from the beginning of
the input. This simultaneous and deterministic process enables it to
effectively perform tokenization, POS tagging, and lemmatization.

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
