%global packname  rSQM
%global packver   1.3.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.14
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Downscaling Toolkit for Climate Change Scenariousing Non Parametric Quantile Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-EcoHydRology 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-mise 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-qmap 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-EcoHydRology 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-mise 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-qmap 
Requires:         R-CRAN-ggplot2 

%description
Conducts statistical downscaling of daily CMIP5 (Coupled Model
Intercomparison Project 5) climate change scenario data at a station level
using empirical quantile mapping method by Jaepil Cho et al. (2016)
<doi:10.1002/ird.2035>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
