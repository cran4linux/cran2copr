%global packname  stplanr
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Sustainable Transport Planning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-geosphere >= 1.5.7
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-igraph >= 1.2.2
BuildRequires:    R-CRAN-maptools >= 0.9.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.100.5.0
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-sf >= 0.6.3
BuildRequires:    R-CRAN-nabor >= 0.5.0
BuildRequires:    R-CRAN-rgeos >= 0.3.28
BuildRequires:    R-CRAN-rlang >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-lwgeom >= 0.1.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-geosphere >= 1.5.7
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-maptools >= 0.9.3
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-sf >= 0.6.3
Requires:         R-CRAN-nabor >= 0.5.0
Requires:         R-CRAN-rgeos >= 0.3.28
Requires:         R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-lwgeom >= 0.1.4
Requires:         R-methods 
Requires:         R-CRAN-magrittr 

%description
Tools for transport planning with an emphasis on spatial transport data
and non-motorized modes. Enables common transport planning tasks
including: downloading and cleaning transport datasets; creating
geographic "desire lines" from origin-destination (OD) data; route
assignment, locally and via interfaces to routing services such as
<http://cyclestreets.net/>; calculation of route segment attributes such
as bearing and aggregate flow; and 'travel watershed' analysis. See
Lovelace and Ellison (2018) <doi:10.32614/RJ-2018-053>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/benchmarks.R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example-flows-up-hill.R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/logo.R
%doc %{rlibdir}/%{packname}/stplanr-logo-vector-only.svg
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
