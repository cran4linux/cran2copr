%global packname  SWMPrExtension
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          2%{?dist}
Summary:          Functions for Analyzing and Plotting Estuary Monitoring Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SWMPr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-SWMPr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-grDevices 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maptools 
Requires:         R-methods 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tidyr 

%description
Tools for performing routine analysis and plotting tasks with
environmental data from the System Wide Monitoring Program of the National
Estuarine Research Reserve System <http://cdmo.baruch.sc.edu/>. This
package builds on the functionality of the SWMPr package
<https://cran.r-project.org/package=SWMPr>, which is used to retrieve and
organize the data. The combined set of tools address common challenges
associated with continuous time series data for environmental decision
making, and are intended for use in annual reporting activities.
References: Beck, Marcus W. (2016) <ISSN
2073-4859><https://journal.r-project.org/archive/2016-1/beck.pdf> Rudis,
Bob (2014)
<https://rud.is/b/2014/11/16/moving-the-earth-well-alaska-hawaii-with-r/>.
United States Environmental Protection Agency (2015)
<https://cfpub.epa.gov/si/si_public_record_Report.cfm?dirEntryId=327030>.
United States Environmental Protection Agency (2012)
<http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.646.1973&rep=rep1&type=pdf>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
