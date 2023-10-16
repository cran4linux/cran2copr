%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  saeHB.unit
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Unit Level Model using Hierarchical Bayesian Approach

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.60
Requires:         R-core >= 3.60
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-rjags 
Requires:         R-stats 

%description
Small area estimation unit level models (Battese-Harter-Fuller model) with
a Bayesian Hierarchical approach. See also Rao & Molina (2015,
ISBN:978-1-118-73578-7) and Battese et al. (1988)
<doi:10.1080/01621459.1988.10478561>.

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
