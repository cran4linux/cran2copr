%global __brp_check_rpaths %{nil}
%global packname  spatialRF
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Spatial Modeling with Random Forest

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-huxtable 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-huxtable 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-viridis 

%description
Automatic generation and selection of spatial predictors for spatial
regression with Random Forest. Spatial predictors are surrogates of
variables driving the spatial structure of a response variable. The
package offers two methods to generate spatial predictors from a distance
matrix among training cases: 1) Moran's Eigenvector Maps (MEMs; Dray,
Legendre, and Peres-Neto 2006 <DOI:10.1016/j.ecolmodel.2006.02.015>):
computed as the eigenvectors of a weighted matrix of distances; 2) RFsp
(Hengl et al. <DOI:10.7717/peerj.5518>): columns of the distance matrix
used as spatial predictors. Spatial predictors help minimize the spatial
autocorrelation of the model residuals and facilitate an honest assessment
of the importance scores of the non-spatial predictors. Additionally,
functions to reduce multicollinearity, identify relevant variable
interactions, tune random forest hyperparameters, assess model
transferability via spatial cross-validation, and explore model results
via partial dependence curves and interaction surfaces are included in the
package. The modelling functions are built around the highly efficient
'ranger' package (Wright and Ziegler 2017 <DOI:10.18637/jss.v077.i01>).

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
