%global __brp_check_rpaths %{nil}
%global packname  ggExtra
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Add Marginal Histograms to 'ggplot2', and More 'ggplot2' Enhancements

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-grid >= 3.1.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-colourpicker >= 1.0
BuildRequires:    R-CRAN-shinyjs >= 0.5.2
BuildRequires:    R-CRAN-gtable >= 0.2.0
BuildRequires:    R-CRAN-scales >= 0.2.0
BuildRequires:    R-CRAN-shiny >= 0.13.0
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
Requires:         R-grid >= 3.1.3
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-colourpicker >= 1.0
Requires:         R-CRAN-shinyjs >= 0.5.2
Requires:         R-CRAN-gtable >= 0.2.0
Requires:         R-CRAN-scales >= 0.2.0
Requires:         R-CRAN-shiny >= 0.13.0
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-R6 

%description
Collection of functions and layers to enhance 'ggplot2'. The flagship
function is 'ggMarginal()', which can be used to add marginal
histograms/boxplots/density plots to 'ggplot2' scatterplots.

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
