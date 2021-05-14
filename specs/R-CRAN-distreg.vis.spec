%global packname  distreg.vis
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Framework for the Visualization of Distributional Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss.dist >= 5.1.0
BuildRequires:    R-CRAN-gamlss >= 5.0.6
BuildRequires:    R-CRAN-betareg >= 3.1.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-formatR >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-rhandsontable >= 0.3.4
BuildRequires:    R-CRAN-bamlss >= 0.1.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-gamlss.dist >= 5.1.0
Requires:         R-CRAN-gamlss >= 5.0.6
Requires:         R-CRAN-betareg >= 3.1.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-formatR >= 1.5
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-rhandsontable >= 0.3.4
Requires:         R-CRAN-bamlss >= 0.1.2
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Functions for visualizing distributional regression models fitted using
the 'gamlss', 'bamlss' or 'betareg' R package. The core of the package
consists of a 'shiny' application, where the model results can be
interactively explored and visualized.

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
