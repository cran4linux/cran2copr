%global packname  HDiR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Directional Highest Density Regions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NPCirc 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Directional 
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-NPCirc 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Directional 
Requires:         R-CRAN-movMF 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 

%description
We provide an R tool for nonparametric plug-in estimation of Highest
Density Regions (HDRs) in the directional setting. Concretely, circular
and spherical regions can be reconstructed from a data sample following
Saavedra-Nieves and Crujeiras (2020) <arXiv:2009.08915>. This library also
contains two real datasets in the circular and spherical settings. The
first one concerns a problem from animal orientation studies and the
second one is related to earthquakes occurrences.

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
