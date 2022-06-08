%global __brp_check_rpaths %{nil}
%global packname  pedprobr
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Probability Computations on Pedigrees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 1.1.0
BuildRequires:    R-CRAN-pedmut 
Requires:         R-CRAN-pedtools >= 1.1.0
Requires:         R-CRAN-pedmut 

%description
An implementation of the Elston-Stewart algorithm for calculating pedigree
likelihoods given genetic marker data (Elston and Stewart (1971)
<doi:10.1159/000152448>). The standard algorithm is extended to allow
inbred founders. 'pedprobr' is part of the 'ped suite', a collection of
packages for pedigree analysis in R. In particular, 'pedprobr' depends on
'pedtools' for pedigree manipulations and 'pedmut' for mutation modelling.
For more information, see 'Pedigree Analysis in R' (Vigeland, 2021,
ISBN:9780128244302).

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
