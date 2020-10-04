%global packname  countyfloods
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Quantify United States County-Level Flood Measurements

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-grid >= 3.2.5
BuildRequires:    R-CRAN-maps >= 3.1.1
BuildRequires:    R-CRAN-dataRetrieval >= 2.5.10
BuildRequires:    R-CRAN-R.utils >= 2.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-tidyr >= 0.6.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
Requires:         R-grid >= 3.2.5
Requires:         R-CRAN-maps >= 3.1.1
Requires:         R-CRAN-dataRetrieval >= 2.5.10
Requires:         R-CRAN-R.utils >= 2.5.0
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-tidyr >= 0.6.0
Requires:         R-CRAN-dplyr >= 0.5.0

%description
Quantifies United States flood impacts at the county level using United
States Geological Service (USGS) River Discharge data for the USGS API.
This package builds on R packages from the USGS, with the goal of creating
county-level time series of flood status that can be more easily joined
with county-level impact measurements, including health outcomes. This
work was supported in part by grants from the National Institute of
Environmental Health Sciences (R00ES022631), the Colorado Water Center,
and the National Science Foundation, Integrative Graduate Education and
Research Traineeship (IGERT) Grant No. DGE-0966346 "I-WATER: Integrated
Water, Atmosphere, Ecosystems Education and Research Program" at Colorado
State University.

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
%{rlibdir}/%{packname}/INDEX
