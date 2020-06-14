%global packname  UScensus2000cdp
%global packver   0.03
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.03
Release:          2%{?dist}
Summary:          US Census 2000 Designated Places Shapefiles and AdditionalDemographic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-foreign 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-sp 
Requires:         R-foreign 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-utils 

%description
US Census 2000 Designated Places shapefiles and additional demographic
data from the SF1 100 percent files. This data set contains polygon files
in lat/lon coordinates and the corresponding demographic data for a number
of different variables.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
