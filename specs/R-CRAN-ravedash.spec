%global __brp_check_rpaths %{nil}
%global packname  ravedash
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dashboard System for Reproducible Visualization of 'iEEG'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-shinyWidgets >= 0.6.2
BuildRequires:    R-CRAN-threeBrain >= 0.2.4
BuildRequires:    R-CRAN-logger >= 0.2.2
BuildRequires:    R-CRAN-dipsaus >= 0.2.0
BuildRequires:    R-CRAN-rpymat >= 0.1.2
BuildRequires:    R-CRAN-shidashi >= 0.1.0.9000
BuildRequires:    R-CRAN-raveio >= 0.0.5.9000
BuildRequires:    R-CRAN-shinyvalidate 
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-shinyWidgets >= 0.6.2
Requires:         R-CRAN-threeBrain >= 0.2.4
Requires:         R-CRAN-logger >= 0.2.2
Requires:         R-CRAN-dipsaus >= 0.2.0
Requires:         R-CRAN-rpymat >= 0.1.2
Requires:         R-CRAN-shidashi >= 0.1.0.9000
Requires:         R-CRAN-raveio >= 0.0.5.9000
Requires:         R-CRAN-shinyvalidate 

%description
Dashboard system to display the analysis results produced by 'RAVE'
(Magnotti J.F., Wang Z., Beauchamp M.S. (2020), R analysis and
visualizations of 'iEEG' <doi:10.1016/j.neuroimage.2020.117341>). Provides
infrastructure to integrate customized analysis pipelines into dashboard
modules, including file structures, front-end widgets, and event handlers.

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
