%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EvolutionaryGames
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Important Concepts of Evolutionary Game Theory

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.43
BuildRequires:    R-grDevices >= 3.2.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-deSolve >= 1.14
BuildRequires:    R-CRAN-interp >= 1.0.29
BuildRequires:    R-CRAN-geometry >= 0.3.6
Requires:         R-CRAN-MASS >= 7.3.43
Requires:         R-grDevices >= 3.2.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-deSolve >= 1.14
Requires:         R-CRAN-interp >= 1.0.29
Requires:         R-CRAN-geometry >= 0.3.6

%description
Evolutionary game theory applies game theory to evolving populations in
biology, see e.g. one of the books by Weibull (1994, ISBN:978-0262731218)
or by Sandholm (2010, ISBN:978-0262195874) for more details. A
comprehensive set of tools to illustrate the core concepts of evolutionary
game theory, such as evolutionary stability or various evolutionary
dynamics, for teaching and academic research is provided.

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
