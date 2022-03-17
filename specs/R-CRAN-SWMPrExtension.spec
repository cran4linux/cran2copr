%global __brp_check_rpaths %{nil}
%global packname  SWMPrExtension
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Analyzing and Plotting Estuary Monitoring Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SWMPr 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggimage 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-SWMPr 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggimage 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-grDevices 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Tools for performing routine analysis and plotting tasks with
environmental data from the System Wide Monitoring Program of the National
Estuarine Research Reserve System <http://cdmo.baruch.sc.edu/>. This
package builds on the functionality of the 'SWMPr' package
<https://cran.r-project.org/package=SWMPr>, which is used to retrieve and
organize the data. The combined set of tools address common challenges
associated with continuous time series data for environmental decision
making, and are intended for use in annual reporting activities.
References: Beck, Marcus W. (2016) <ISSN
2073-4859><https://journal.r-project.org/archive/2016-1/beck.pdf> Rudis,
Bob (2014)
<https://rud.is/b/2014/11/16/moving-the-earth-well-alaska-hawaii-with-r/>.
United States Environmental Protection Agency (2015)
<https://cfpub.epa.gov/si/si_public_record_Report.cfm?Lab=OWOW&dirEntryId=327030>.
United States Environmental Protection Agency (2012)
<http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.646.1973&rep=rep1&type=pdf>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
