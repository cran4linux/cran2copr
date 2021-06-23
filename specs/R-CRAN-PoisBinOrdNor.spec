%global __brp_check_rpaths %{nil}
%global packname  PoisBinOrdNor
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Data Generation with Poisson, Binary, Ordinal and Normal Components

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-GenOrd 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-GenOrd 

%description
Generation of multiple count, binary, ordinal and normal variables
simultaneously given the marginal characteristics and association
structure. The details of the method are explained in Demirtas et al.
(2012) <DOI:10.1002/sim.5362>.

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
