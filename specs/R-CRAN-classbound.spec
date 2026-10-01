%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  classbound
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization for Classification Decision Boundaries

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-class 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-RColorBrewer 

%description
Exploring, visualizing, and comparing classification decision boundaries.
Provides a unified interface for fitting classifiers and rendering 2D
decision boundary plots, with support for 2D slice visualization (fixing
non-plotted dimensions at reference values) and projection-based
visualization for high-dimensional data (including Principal Component
Analysis (PCA) and tour projections from the 'tourr' package). Supports
native 'R' classifiers, 'tidymodels' workflows, and custom user-supplied
models via a flexible adapter system. Includes an interactive 'Shiny'
application ('explorapp') for visual exploration, data simulation,
drawing, model comparison, probability surfaces, and reproducible exports.

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
