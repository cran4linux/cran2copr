%global __brp_check_rpaths %{nil}
%global packname  CoopGame
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Important Concepts of Cooperative Game Theory

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-methods >= 3.3.1
BuildRequires:    R-CRAN-rcdd >= 1.1
BuildRequires:    R-CRAN-geometry >= 0.3.6
BuildRequires:    R-utils 
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-methods >= 3.3.1
Requires:         R-CRAN-rcdd >= 1.1
Requires:         R-CRAN-geometry >= 0.3.6
Requires:         R-utils 

%description
The theory of cooperative games with transferable utility offers useful
insights into the way parties can share gains from cooperation and secure
sustainable agreements, see e.g. one of the books by Chakravarty, Mitra
and Sarkar (2015, ISBN:978-1107058798) or by Driessen (1988,
ISBN:978-9027727299) for more details. A comprehensive set of tools for
cooperative game theory with transferable utility is provided. Users can
create special families of cooperative games, like e.g. bankruptcy games,
cost sharing games and weighted voting games. There are functions to check
various game properties and to compute five different set-valued solution
concepts for cooperative games. A large number of point-valued solution
concepts is available reflecting the diverse application areas of
cooperative game theory. Some of these point-valued solution concepts can
be used to analyze weighted voting games and measure the influence of
individual voters within a voting body. There are routines for visualizing
both set-valued and point-valued solutions in the case of three or four
players.

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
