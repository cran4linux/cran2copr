%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  muiCharts
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'MUI X Charts' for 'shiny' Apps and 'Quarto'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny.react >= 0.4.0
BuildRequires:    R-CRAN-muiMaterial >= 0.2.1
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny.react >= 0.4.0
Requires:         R-CRAN-muiMaterial >= 0.2.1
Requires:         R-CRAN-htmltools 
Requires:         R-utils 

%description
'MUI X Charts' React chart components for data visualization for building
'shiny' applications and 'quarto' documents. Bundles the MIT-licensed
community edition of the '@mui/x-charts' JavaScript library (the
commercial 'Pro' tier is not included).

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
