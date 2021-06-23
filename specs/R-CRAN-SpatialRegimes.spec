%global __brp_check_rpaths %{nil}
%global packname  SpatialRegimes
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Constrained Clusterwise Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-GWmodel 
BuildRequires:    R-CRAN-plm 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-GWmodel 
Requires:         R-CRAN-plm 

%description
A collection of functions for estimating spatial regimes, aggregations of
neighboring spatial units that are homogeneous in functional terms. The
term spatial regime, therefore, should not be understood as a synonym for
cluster. More precisely, the term cluster does not presuppose any
functional relationship between the variables considered, while the term
regime is linked to a regressive relationship underlying the spatial
process. For more information, please see Postiglione, P., Andreano, M.S.,
Benedetti R. (2013) <doi:10.1007/s10614-012-9325-z> , Andreano, M.S.,
Benedetti, R., and Postiglione, P. (2017) <doi:10.1007/s11135-016-0415-1>
, Bille', A.G., Benedetti, R., and Postiglione, P. (2017)
<doi:10.1080/17421772.2017.1286373>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
