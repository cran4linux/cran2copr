%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simboot
%global packver   0.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous Inference for Diversity Indices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-mvtnorm 

%description
Provides estimation of simultaneous bootstrap and asymptotic confidence
intervals for diversity indices, namely the Shannon and the Simpson index.
Several pre--specified multiple comparison types are available to choose.
Further user--defined contrast matrices are applicable. In addition,
simboot estimates adjusted as well as unadjusted p--values for two of the
three proposed bootstrap methods. Further simboot allows for comparing
biological diversities of two or more groups while simultaneously testing
a user-defined selection of Hill numbers of orders q, which are considered
as appropriate and useful indices for measuring diversity.

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
