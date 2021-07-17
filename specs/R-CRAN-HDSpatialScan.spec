%global __brp_check_rpaths %{nil}
%global packname  HDSpatialScan
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate and Functional Spatial Scan Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-SpatialNP 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-swfscMisc 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-SpatialNP 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-swfscMisc 
Requires:         R-CRAN-rgeos 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Allows to detect spatial clusters of abnormal values on multivariate or
functional data. Martin KULLDORFF and Lan HUANG and Kevin KONTY (2009)
<doi:10.1186/1476-072X-8-58>, Inkyung JUNG and Ho Jin CHO (2015)
<doi:10.1186/s12942-015-0024-6>, Lionel CUCALA and Michael GENIN and
Caroline LANIER and Florent OCCELLI (2017)
<doi:10.1016/j.spasta.2017.06.001>, Lionel CUCALA and Michael GENIN and
Florent OCCELLI and Julien SOULA (2019)
<doi:10.1016/j.spasta.2018.10.002>, Zaineb SMIDA and Lionel CUCALA and Ali
GANNOUN (2020) <https://hal.archives-ouvertes.fr/hal-02908496>, Camille
FREVENT and Mohamed-Salem AHMED and Matthieu MARBAC and Michael GENIN
(2021) <arXiv:2011.03482>, Camille FREVENT and Mohamed-Salem AHMED and
Sophie DABO-NIANG and Michael GENIN (2021) <arXiv:2103.14401>.

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
