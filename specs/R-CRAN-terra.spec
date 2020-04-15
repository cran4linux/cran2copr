%global packname  terra
%global packver   0.5-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          1%{?dist}
Summary:          Classes and Methods for Spatial Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-raster >= 3.0.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-raster >= 3.0.12
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Classes and methods for spatial data, especially raster data. Methods
allow for low-level data manipulation as well as high-level global, local,
zonal, and focal computation. The predict and interpolate methods
facilitate the use of regression type (interpolation, machine learning)
models for spatial prediction. The user-interface is very similar to that
of the 'raster' package; but it is simpler and faster. Processing of very
large files is supported. See the manual and tutorials on
<https://rspatial.org/terra/> to get started.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/exdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
