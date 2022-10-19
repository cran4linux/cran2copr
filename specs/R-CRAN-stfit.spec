%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stfit
%global packver   0.99.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.9
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Functional Imputation Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-RColorBrewer 

%description
A general spatiotemporal satellite image imputation method based on sparse
functional data analytic techniques. The imputation method applies and
extends the Functional Principal Analysis by Conditional Estimation
(PACE). The underlying idea for the proposed procedure is to impute a
missing pixel by borrowing information from temporally and spatially
contiguous pixels based on the best linear unbiased prediction.

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
