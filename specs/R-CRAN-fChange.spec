%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fChange
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Change Point Detection and Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastmatrix 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-ftsa 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rainbow 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vars 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastmatrix 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-ftsa 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rainbow 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vars 

%description
Analyze functional data and its change points. Includes functionality to
store and process data, summarize and validate assumptions, characterize
and perform inference of change points, and provide visualizations. Data
is stored as discretely collected observations without requiring the
selection of basis functions. For more details see chapter 8 of Horvath
and Rice (2024) <doi:10.1007/978-3-031-51609-2>. Additional papers are
forthcoming. Focused works are also included in the documentation of
corresponding functions.

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
