%global __brp_check_rpaths %{nil}
%global packname  gamblers.ruin.gameplay
%global packver   4.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          One-Dimensional Random Walks Through Simulation of the Gambler's Ruin Problem

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-viridis 

%description
Simulates a gambling game under the gambler's ruin setup, after asking for
the money you have and the money you want to win, along with your win
probability in each round of the game.

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
