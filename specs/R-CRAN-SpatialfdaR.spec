%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatialfdaR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Functional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-fda 
Requires:         R-splines 
Requires:         R-graphics 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
Finite element modeling (FEM) uses meshes of triangles to define surfaces.
A surface within a triangle may be either linear or quadratic. In the
order one case each node in the mesh is associated with a basis function
and the basis is called the order one finite element basis. In the order
two case each edge mid-point is also associated with a basis function.
Functions are provided for smoothing, density function estimation point
evaluation and plotting results.  Two papers illustrating the finite
element data analysis are Sangalli, L.M., Ramsay, J.O., Ramsay, T.O.
(2013)<http://www.mox.polimi.it/~sangalli> and Bernardi, M.S, Carey, M.,
Ramsay, J. O., Sangalli, L. (2018)<http://www.mox.polimi.it/~sangalli>.
Modelling spatial anisotropy via regression with partial differential
regularization Journal of Multivariate Analysis, 167, 15-30.

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
