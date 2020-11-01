%global packname  IsoSpecR
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          The IsoSpec Algorithm

License:          BSD_2_clause + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-Rcpp >= 0.12.0

%description
IsoSpec is a fine structure calculator used for obtaining the most
probable masses of a chemical compound given the frequencies of the
composing isotopes and their masses. It finds the smallest set of
isotopologues with a given probability. The probability is assumed to be
that of the product of multinomial distributions, each corresponding to
one particular element and parametrized by the frequencies of finding
these elements in nature. These numbers are supplied by IUPAC - the
International Union of Pure and Applied Chemistry. See: Lacki, Valkenborg,
Startek (2020) <DOI:10.1021/acs.analchem.0c00959> and Lacki, Startek,
Valkenborg, Gambin (2017) <DOI:10.1021/acs.analchem.6b01459> for the
description of the algorithms used.

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
