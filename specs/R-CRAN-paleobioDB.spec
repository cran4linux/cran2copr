%global packname  paleobioDB
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          2%{?dist}
Summary:          Download and Process Data from the Paleobiology Database

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 

%description
Includes 19 functions to wrap each endpoint of the PaleobioDB API, plus 8
functions to visualize and process the fossil data. The API documentation
for the Paleobiology Database can be found in
<http://paleobiodb.org/data1.1/>.

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
%{rlibdir}/%{packname}/INDEX
