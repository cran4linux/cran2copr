%global packname  raster
%global packver   3.0-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.12
Release:          1%{?dist}
Summary:          Geographic Data Analysis and Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 

%description
Reading, writing, manipulating, analyzing and modeling of gridded spatial
data. The package implements basic and high-level functions. Processing of
very large files is supported. There is a also support for vector data
operations such as intersections. See the manual and tutorials on
<https://rspatial.org/> to get started.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
