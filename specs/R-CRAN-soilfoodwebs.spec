%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soilfoodwebs
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Soil Food Web Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve >= 5.6.15
BuildRequires:    R-graphics >= 4.1.0
BuildRequires:    R-CRAN-rootSolve >= 1.8.2.2
BuildRequires:    R-CRAN-diagram >= 1.6.5
BuildRequires:    R-CRAN-quadprog >= 1.5.8
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-deSolve >= 1.28
Requires:         R-CRAN-lpSolve >= 5.6.15
Requires:         R-graphics >= 4.1.0
Requires:         R-CRAN-rootSolve >= 1.8.2.2
Requires:         R-CRAN-diagram >= 1.6.5
Requires:         R-CRAN-quadprog >= 1.5.8
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-deSolve >= 1.28

%description
Analyzing soil food webs or any food web measured at equilibrium. The
package calculates carbon and nitrogen fluxes and stability properties
using methods described by Hunt et al. (1987) <doi:10.1007/BF00260580>, de
Ruiter et al. (1995) <doi:10.1126/science.269.5228.1257>, Holtkamp et al.
(2011) <doi:10.1016/j.soilbio.2010.10.004>, and Buchkowski and Lindo
(2021) <doi:10.1111/1365-2435.13706>. The package can also manipulate the
structure of the food web as well as simulate food webs away from
equilibrium and run decomposition experiments.

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
