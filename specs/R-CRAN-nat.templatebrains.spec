%global packname  nat.templatebrains
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          NeuroAnatomy Toolbox ('nat') Extension for Handling Template Brains

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-nat >= 1.8.6
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-nat >= 1.8.6
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-rappdirs 

%description
Extends package 'nat' (NeuroAnatomy Toolbox) by providing objects and
functions for handling template brains.

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
