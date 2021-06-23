%global __brp_check_rpaths %{nil}
%global packname  gamlss.mx
%global packver   6.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Mixture Distributions with GAMLSS

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.1
Requires:         R-core >= 2.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-nnet 
Requires:         R-stats 
Requires:         R-graphics 

%description
The main purpose of this package is to allow fitting of mixture
distributions with generalised additive models for location scale and
shape models see Chapter 7 of Stasinopoulos et al. (2017)
<doi:10.1201/b21973-4>.

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
