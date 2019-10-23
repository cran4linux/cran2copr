%global packname  gridsample
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Tools for Grid-Based Survey Sampling Design

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-geosphere >= 1.5.5
BuildRequires:    R-CRAN-spatstat >= 1.49.0
BuildRequires:    R-CRAN-rgdal >= 1.2.4
BuildRequires:    R-CRAN-sp >= 1.2.4
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-maptools >= 0.8.41
BuildRequires:    R-CRAN-rgeos >= 0.3.21
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spatstat.utils 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-geosphere >= 1.5.5
Requires:         R-CRAN-spatstat >= 1.49.0
Requires:         R-CRAN-rgdal >= 1.2.4
Requires:         R-CRAN-sp >= 1.2.4
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-maptools >= 0.8.41
Requires:         R-CRAN-rgeos >= 0.3.21
Requires:         R-methods 
Requires:         R-CRAN-spatstat.utils 

%description
Multi-stage cluster surveys of households are commonly performed by
governments and programmes to monitor population-level demographic,
social, economic, and health outcomes. Generally, communities are sampled
from subpopulations (strata) in a first stage, and then households are
listed and sampled in a second stage. In this typical two-stage design,
sampled communities are the Primary Sampling Units (PSUs) and households
are the Secondary Sampling Units (SSUs). Census data typically serve as
the sample frame from which PSUs are selected. However, if census data are
outdated inaccurate, or too geographically course, gridded population data
(such as <http://www.worldpop.org.uk>) can be used as a sample frame
instead. GridSample (<doi:10.1186/s12942-017-0098-4>) generates PSUs from
gridded population data according to user-specified complex survey design
characteristics and household sample size. In gridded population sampling,
like census sampling, PSUs are selected within each stratum using a
serpentine sampling method, and can be oversampled in urban or rural areas
to ensure a minimum sample size in each of these important sub-domains.
Furthermore, because grid cells are uniform in size and shape, gridded
population sampling allows for samples to be representative of both the
population and of space, which is not possible with a census sample frame.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
