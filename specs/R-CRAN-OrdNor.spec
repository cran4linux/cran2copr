%global __brp_check_rpaths %{nil}
%global packname  OrdNor
%global packver   2.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Concurrent Generation of Ordinal and Normal Data with Given Correlation Matrix and Marginal Distributions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-GenOrd 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-GenOrd 
Requires:         R-stats 

%description
Implementation of a procedure for generating samples from a mixed
distribution of ordinal and normal random variables with a pre-specified
correlation matrix and marginal distributions. The details of the method
are explained in Demirtas et al. (2015)
<DOI:10.1080/10543406.2014.920868>.

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
