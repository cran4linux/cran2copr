%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  polarisR
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Linear Dimensionality Reduction Visualization Tool

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-detourr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-quollr 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tourr 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-utils 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-detourr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-quollr 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-tourr 
Requires:         R-CRAN-umap 
Requires:         R-utils 

%description
A 'shiny' application for visualizing high-dimensional data using
non-linear dimensionality reduction (NLDR) techniques such as t-SNE and
UMAP. It provides an interactive platform to explore high-dimensional
datasets, diagnose the quality of the embeddings using the 'quollr'
package, and compare different NLDR methods.

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
