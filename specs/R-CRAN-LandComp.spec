%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LandComp
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analysing Landscape Composition and Structure at Multiple Scales

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-sf 

%description
Changes of landscape diversity and structure can be detected soon if
relying on landscape class combinations and analysing patterns at multiple
scales. 'LandComp' provides such an opportunity, based on Juhász-Nagy's
functions (Juhász-Nagy P, Podani J 1983 <doi:10.1007/BF00129432>).
Functions can handle multilayered data. Requirements of the input: binary
data contained by a regular square or hexagonal grid, and the grid should
have projected coordinates.

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
