%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wallace
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Modular Platform for Reproducible Modeling of Species Niches and Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ecospat >= 4.0.0
BuildRequires:    R-CRAN-ENMeval >= 2.0.3
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-spocc >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-leaflet.extras >= 1.0.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.6.0
BuildRequires:    R-CRAN-DT >= 0.5
BuildRequires:    R-CRAN-knitcitations 
BuildRequires:    R-CRAN-leafem 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-spThin 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-ecospat >= 4.0.0
Requires:         R-CRAN-ENMeval >= 2.0.3
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-spocc >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-leaflet.extras >= 1.0.0
Requires:         R-CRAN-shinyWidgets >= 0.6.0
Requires:         R-CRAN-DT >= 0.5
Requires:         R-CRAN-knitcitations 
Requires:         R-CRAN-leafem 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-spThin 
Requires:         R-CRAN-zip 

%description
The 'shiny' application Wallace is a modular platform for reproducible
modeling of species niches and distributions. Wallace guides users through
a complete analysis, from the acquisition of species occurrence and
environmental data to visualizing model predictions on an interactive map,
thus bundling complex workflows into a single, streamlined interface. An
extensive vignette, which guides users through most package functionality
can be found on the package's GitHub Pages website:
<https://wallaceecomod.github.io/wallace/articles/tutorial-v2.html>.

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
