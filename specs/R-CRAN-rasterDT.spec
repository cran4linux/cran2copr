%global packname  rasterDT
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Fast Raster Summary and Manipulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-sf 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fasterize 
Requires:         R-CRAN-sf 

%description
Fast alternatives to several relatively slow 'raster' package functions.
For large rasters, the functions run from 5 to approximately 100 times
faster than the 'raster' package functions they replace. The 'fasterize'
package, on which one function in this package depends, includes an
implementation of the scan line algorithm attributed to Wylie et al.
(1967) <doi:10.1145/1465611.1465619>.

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
%{rlibdir}/%{packname}/INDEX
