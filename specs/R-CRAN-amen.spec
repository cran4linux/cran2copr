%global __brp_check_rpaths %{nil}
%global packname  amen
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Additive and Multiplicative Effects Models for Networks and Relational Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Analysis of dyadic network and relational data using additive and
multiplicative effects (AME) models. The basic model includes regression
terms, the covariance structure of the social relations model (Warner,
Kenny and Stoto (1979) <DOI:10.1037/0022-3514.37.10.1742>, Wong (1982)
<DOI:10.2307/2287296>), and multiplicative factor models (Hoff(2009)
<DOI:10.1007/s10588-008-9040-4>). Several different link functions
accommodate different relational data structures, including binary/network
data, normal relational data, zero-inflated positive outcomes using a
tobit model, ordinal relational data and data from fixed-rank nomination
schemes. Several of these link functions are discussed in Hoff, Fosdick,
Volfovsky and Stovel (2013) <DOI:10.1017/nws.2013.17>. Development of this
software was supported in part by NIH grant R01HD067509.

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
