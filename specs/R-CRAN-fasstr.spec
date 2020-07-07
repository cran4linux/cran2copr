%global packname  fasstr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Analyze, Summarize, and Visualize Daily Streamflow Data

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-PearsonDS >= 1.1
BuildRequires:    R-CRAN-fitdistrplus >= 1.0.14
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-tidyhydat >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-RcppRoll >= 0.3.0
BuildRequires:    R-CRAN-zyp >= 0.10.1.1
BuildRequires:    R-grDevices 
Requires:         R-CRAN-openxlsx >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-PearsonDS >= 1.1
Requires:         R-CRAN-fitdistrplus >= 1.0.14
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-tidyhydat >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-RcppRoll >= 0.3.0
Requires:         R-CRAN-zyp >= 0.10.1.1
Requires:         R-grDevices 

%description
The Flow Analysis Summary Statistics Tool for R, 'fasstr', provides
various functions to clean and screen daily stream discharge data;
calculate and visualize various summary statistics and metrics; and
compute annual trending (using 'zyp' package methods
<https://CRAN.R-project.org/package=zyp>) and volume frequency analyses
(using methods similar to HEC-SSP (2019)
<https://www.hec.usace.army.mil/software/hec-ssp/>). It features useful
function arguments for filtering of and handling dates, customizing data
and metrics, and the ability to pull daily data directly from the Water
Survey of Canada hydrometric database
(<https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/>).

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
%{rlibdir}/%{packname}/INDEX
