%global __brp_check_rpaths %{nil}
%global packname  layer
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tilts your Maps and Turns Them into Ggplot Objects

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scico 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggnewscale 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scico 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggnewscale 

%description
Simplifies the whole process of creating stacked tilted maps, that are
often used in scientific publications to show different environmental
layers for a geographical region. Tilting maps and layering them allows to
easily draw visual correlations between these environmental layers.

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
