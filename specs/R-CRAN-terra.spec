%global packname  terra
%global packver   0.6-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.9
Release:          2%{?dist}
Summary:          Spatial Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-raster >= 3.1.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-raster >= 3.1.5
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Methods for spatial data analysis, especially raster data. Methods allow
for low-level data manipulation as well as high-level global, local,
zonal, and focal computation. The predict and interpolate methods
facilitate the use of regression type (interpolation, machine learning)
models for spatial prediction. Processing of very large files is
supported. See the manual and tutorials on <https://rspatial.org/terra/>
to get started. The package is similar to the 'raster' package; but it is
simpler and faster.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ex
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
