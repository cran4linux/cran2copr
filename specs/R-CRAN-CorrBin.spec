%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CorrBin
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametrics with Clustered Binary and Multinomial Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-dirmult 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-dirmult 
Requires:         R-CRAN-mvtnorm 

%description
Implements non-parametric analyses for clustered binary and multinomial
data. The elements of the cluster are assumed exchangeable, and identical
joint distribution (also known as marginal compatibility, or
reproducibility) is assumed for clusters of different sizes. A trend test
based on stochastic ordering is implemented. Szabo A, George EO. (2010)
<doi:10.1093/biomet/asp077>; George EO, Cheon K, Yuan Y, Szabo A (2016)
<doi:10.1093/biomet/asw009>.

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
