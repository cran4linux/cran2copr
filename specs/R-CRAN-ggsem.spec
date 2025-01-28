%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggsem
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interactively Visualize Structural Equation Modeling Diagrams

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-smplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-umap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-colourpicker 
Requires:         R-grid 
Requires:         R-CRAN-svglite 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-smplot2 
Requires:         R-utils 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-umap 

%description
It is an R package and web-based application, allowing users to perform
interactive and reproducible visualizations of path diagrams for
structural equation modeling (SEM) and networks using the 'ggplot2'
engine. Its app (built with 'shiny') provides an interface that allows
extensive customization, and creates CSV outputs, which can then be used
to recreate the figures either using the web app or script-based workflow.

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
