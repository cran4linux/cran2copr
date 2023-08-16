%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pfr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'C++' Library 'Pf'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-inline >= 0.3.19
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-methods 
Requires:         R-CRAN-inline >= 0.3.19
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-methods 

%description
Builds and runs 'c++' code for classes that encapsulate state space model,
particle filtering algorithm pairs. Algorithms include the Bootstrap
Filter from Gordon et al. (1993) <doi:10.1049/ip-f-2.1993.0015>, the
generic SISR filter, the Auxiliary Particle Filter from Pitt et al (1999)
<doi:10.2307/2670179>, and a variety of Rao-Blackwellized particle filters
inspired by Andrieu et al. (2002) <doi:10.1111/1467-9868.00363>. For more
details on the 'c++' library 'pf', see Brown (2020)
<doi:10.21105/joss.02599>.

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
