%global packname  gdalUtilities
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Wrappers for 'GDAL' Utilities Executables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 

%description
R's 'sf' package ships with self-contained 'GDAL' executables, including a
bare bones interface to several of the 'GDAL'-related utility programs
collectively known as the 'GDAL' utilities. For each of those utilities,
this package provides an R wrapper whose formal arguments closely mirror
those of the 'GDAL' command line interface. All of the utilities operate
on data stored in files and typically write their output to other files.
As a result, processing data stored in any of R's more common spatial
formats (i.e. those supported by the 'sp', 'sf', and 'raster' packages)
will require first writing to disk, then processing with the package's
wrapper functions before reading back into R.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
