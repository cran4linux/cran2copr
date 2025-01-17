%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  unhcrthemes
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          UNHCR 'ggplot2' Theme and Colour Palettes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-extrafont 

%description
A 'ggplot2' theme and color palettes following the United Nations High
Commissioner for Refugees (UNHCR) Data Visualization Guidelines
recommendations.

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
