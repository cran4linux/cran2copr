%global packname  raincpc
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Obtain and Analyze Daily Rainfall Data from the USA ClimatePrediction Center (CPC)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-raster 

%description
The Climate Prediction Center's (CPC) rainfall data for the world (1979 to
present, 50 km resolution) and the USA (1948 to present, 25 km
resolution), is one of the few high quality, long term, observation based,
daily rainfall products available for free. Although raw data is available
at CPC's ftp site, obtaining, processing and visualizing the data is not
straightforward. There are thousands of files, and file formats and file
extensions have been changing over time. This package provides
functionality to download, process and visualize over 40 years of global
rainfall data and over 70 years of USA rainfall data from CPC.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
