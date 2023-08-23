%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sadists
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Some Additional Distributions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-PDQutils >= 0.1.1
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-orthopolynom 
Requires:         R-CRAN-PDQutils >= 0.1.1
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-orthopolynom 

%description
Provides the density, distribution, quantile and generation functions of
some obscure probability distributions, including the doubly non-central
t, F, Beta, and Eta distributions; the lambda-prime and K-prime; the
upsilon distribution; the (weighted) sum of non-central chi-squares to a
power; the (weighted) sum of log non-central chi-squares; the product of
non-central chi-squares to powers; the product of doubly non-central F
variables; the product of independent normals.

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
