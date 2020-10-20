%global packname  airGRteaching
%global packver   0.2.9.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9.25
Release:          1%{?dist}%{?buildtag}
Summary:          Teaching Hydrological Modelling with the GR Rainfall-Runoff Models ('Shiny' Interface Included)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-airGR >= 1.4.3.52
BuildRequires:    R-CRAN-dygraphs >= 1.1.1.6
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-airGR >= 1.4.3.52
Requires:         R-CRAN-dygraphs >= 1.1.1.6
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-xts 

%description
Add-on package to the 'airGR' package that simplifies its use and is aimed
at being used for teaching hydrology. The package provides 1) three
functions that allow to complete very simply a hydrological modelling
exercise 2) plotting functions to help students to explore observed data
and to interpret the results of calibration and simulation of the GR
('Génie rural') models 3) a 'Shiny' graphical interface that allows for
displaying the impact of model parameters on hydrographs and models
internal variables.

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
