%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coveffectsplot
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Produce Forest Plots to Visualize Covariate Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       pandoc
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-egg 
Requires:         R-grid 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 

%description
Produce forest plots to visualize covariate effects using either the
command line or an interactive 'Shiny' application.

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
