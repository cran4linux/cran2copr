%global packname  WaterML
%global packver   1.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.5
Release:          1%{?dist}
Summary:          Fetch and Analyze Data from 'WaterML' and 'WaterOneFlow' WebServices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
Requires:         R-stats 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 

%description
Lets you connect to any of the 'Consortium of Universities for the
Advancement of Hydrological Science, Inc.' ('CUAHSI') Water Data Center
'WaterOneFlow' web services and read any 'WaterML' time series data file.
To see list of available web services, see <http://hiscentral.cuahsi.org>.
All versions of 'WaterML' (1.0, 1.1 and 2.0) and both types of the web
service protocol ('SOAP' and 'REST') are supported. The package has six
data download functions: GetServices(): show all public web services from
the HIS Central Catalog. HISCentral_GetSites() and
HISCentral_GetSeriesCatalog(): search for sites or time series from the
HIS Central catalog based on geographic bounding box, server, or keyword.
GetVariables(): Show a data.frame with all variables on the server.
GetSites(): Show a data.frame with all sites on the server. GetSiteInfo():
Show what variables, methods and quality control levels are available at
the specific site. GetValues(): Given a site code, variable code, start
time and end time, fetch a data.frame of all the observation time series
data values. The GetValues() function can also parse 'WaterML' data from a
custom URL or from a local file. The package also has five data upload
functions: AddSites(), AddVariables(), AddMethods(), AddSources(), and
AddValues(). These functions can be used for uploading data to a
'HydroServer Lite' Observations Data Model ('ODM') database via the 'JSON'
data upload web service interface.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
