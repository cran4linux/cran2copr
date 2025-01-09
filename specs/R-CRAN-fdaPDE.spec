%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdaPDE
%global packver   1.1-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.21
Release:          1%{?dist}%{?buildtag}
Summary:          Physics-Informed Spatial and Functional Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plot3D 
Requires:         R-methods 

%description
An implementation of regression models with partial differential
regularizations, making use of the Finite Element Method. The models
efficiently handle data distributed over irregularly shaped domains and
can comply with various conditions at the boundaries of the domain. A
priori information about the spatial structure of the phenomenon under
study can be incorporated in the model via the differential
regularization. See Sangalli, L. M. (2021) <doi:10.1111/insr.12444>
"Spatial Regression With Partial Differential Equation Regularisation" for
an overview. The release 1.1-9 requires R (>= 4.2.0) to be installed on
windows machines.

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
