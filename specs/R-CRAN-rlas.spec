%global packname  rlas
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}
Summary:          Read and Write 'las' and 'laz' Binary File Formats Used forRemote Sensing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 

%description
Read and write 'las' and 'laz' binary file formats. The LAS file format is
a public file format for the interchange of 3-dimensional point cloud data
between data users. The LAS specifications are approved by the American
Society for Photogrammetry and Remote Sensing
<https://www.asprs.org/divisions-committees/lidar-division/laser-las-file-format-exchange-activities>.
The LAZ file format is an open and lossless compression scheme for binary
LAS format versions 1.0 to 1.3 <https://laszip.org/>.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
