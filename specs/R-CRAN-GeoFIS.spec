%global __brp_check_rpaths %{nil}
%global packname  GeoFIS
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Data Processing for Decision Making

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-FisPro >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-FisPro >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-sp 
Requires:         R-CRAN-data.tree 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-nnls 

%description
Methods for processing spatial data for decision-making. This package is
an R implementation of methods provided by the open source software GeoFIS
<https://www.geofis.org> (Leroux et al. 2018)
<doi:10.3390/agriculture8060073>. The main functionalities are the
management zone delineation (Pedroso et al. 2010)
<doi:10.1016/j.compag.2009.10.007> and data aggregation (Mora-Herrera et
al. 2020) <doi:10.1016/j.compag.2020.105624>.

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
