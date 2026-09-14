%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SubTS
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tempered Stable Subordinators and Related Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tweedie 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-gsl 
Requires:         R-stats 
Requires:         R-CRAN-tweedie 

%description
Contains methods for the simulation of tempered stable subordinators and
related distributions. Including classical tempered stable (both finite
and infinite variation), rapidly deceasing tempered stable, truncated
stable, truncated tempered stable, generalized Dickman, truncated gamma,
generalized gamma, and p-gamma. For details, see Dassios et al (2019)
<doi:10.1017/jpr.2019.6>, Dassios et al (2020) <doi:10.1145/3368088>,
Grabchak (2021) <doi:10.1016/j.spl.2020.109015>, Grabchak (2026)
<doi:10.48550/arXiv.2604.17732>.

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
