%global __brp_check_rpaths %{nil}
%global packname  mcmcr
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulate MCMC Samples

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-nlist >= 0.3.1
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-extras 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-term 
BuildRequires:    R-CRAN-universals 
BuildRequires:    R-utils 
Requires:         R-CRAN-nlist >= 0.3.1
Requires:         R-CRAN-abind 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-extras 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-term 
Requires:         R-CRAN-universals 
Requires:         R-utils 

%description
Functions and classes to store, manipulate and summarise Monte Carlo
Markov Chain (MCMC) samples. For more information see Brooks et al. (2011)
<isbn:978-1-4200-7941-8>.

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
