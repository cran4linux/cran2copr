%global packname  grainchanger
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Moving-Window and Direct Data Aggregation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-checkmate 
Requires:         R-methods 
Requires:         R-CRAN-usethis 

%description
Data aggregation via moving window or direct methods. Aggregate a
fine-resolution raster to a grid. The moving window method smooths the
surface using a specified function within a moving window of a specified
size and shape prior to aggregation. The direct method simply aggregates
to the grid using the specified function. The package differs from other
packages offering moving window analysis in 2 key ways: 1. The moving
window code has been optimised so that it runs more quickly than
code{raster::focal} or other packages that build on this; 2. It combines
moving window and aggregation in a way which can be effectively
parallelised.

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
%doc %{rlibdir}/%{packname}/raster
%doc %{rlibdir}/%{packname}/shape
%{rlibdir}/%{packname}/INDEX
