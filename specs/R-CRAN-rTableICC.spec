%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rTableICC
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Random Generation of Contingency Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-aster 
BuildRequires:    R-stats 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-aster 
Requires:         R-stats 

%description
Contains functions for random generation of R x C and 2 x 2 x K
contingency tables. In addition to the generation of contingency tables
over predetermined intraclass-correlated clusters, it is possible to
generate contingency tables without intraclass correlations under product
multinomial, multinomial, and Poisson sampling plans. It also consists of
a function for generation of random data from a given discrete probability
distribution function. See Demirhan (2016)
<https://journal.r-project.org/archive/2016-1/demirhan.pdf> for more
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
