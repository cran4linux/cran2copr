%global packname  raster
%global packver   3.3-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.13
Release:          1%{?dist}
Summary:          Geographic Data Analysis and Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sp >= 1.4.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp >= 1.4.1
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 

%description
Reading, writing, manipulating, analyzing and modeling of spatial data.
The package implements basic and high-level functions for raster data and
for vector data operations such as intersections. See the manual and
tutorials on <https://rspatial.org/> to get started.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
