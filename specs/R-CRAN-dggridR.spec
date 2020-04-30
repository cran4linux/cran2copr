%global packname  dggridR
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}
Summary:          Discrete Global Grids

License:          MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 2.1
BuildRequires:    R-CRAN-sp >= 1.2
BuildRequires:    R-CRAN-rgdal >= 1.1
BuildRequires:    R-CRAN-dplyr >= 0.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods >= 3.4.0
Requires:         R-CRAN-ggplot2 >= 2.1
Requires:         R-CRAN-sp >= 1.2
Requires:         R-CRAN-rgdal >= 1.1
Requires:         R-CRAN-dplyr >= 0.4
Requires:         R-CRAN-Rcpp >= 0.12.12

%description
Spatial analyses involving binning require that every bin have the same
area, but this is impossible using a rectangular grid laid over the Earth
or over any projection of the Earth. Discrete global grids use hexagons,
triangles, and diamonds to overcome this issue, overlaying the Earth with
equally-sized bins. This package provides utilities for working with
discrete global grids, along with utilities to aid in plotting such data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
