%global packname  tabularaster
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Tidy Tools for 'Raster' Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-spbabel >= 0.4.8
BuildRequires:    R-CRAN-spex >= 0.4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-gibble 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-spbabel >= 0.4.8
Requires:         R-CRAN-spex >= 0.4.0
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-gibble 
Requires:         R-CRAN-fasterize 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
Facilities to work with vector and raster data in efficient repeatable and
systematic work flow. Missing functionality in existing packages is
included here to allow extraction from raster data with 'simple features'
and 'Spatial' types and to make extraction consistent and straightforward.
Extract cell numbers from raster data and return the cells, values and
weights as a data frame rather than as lists of matrices or vectors. The
functions here allow spatial data to be used without special handling for
the format currently in use.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/tabula_experiments
%{rlibdir}/%{packname}/INDEX
