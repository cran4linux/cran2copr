%global packname  raincpc
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Obtain and Analyze Rainfall Data from the Climate PredictionCenter

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-SDMTools 
Requires:         R-CRAN-SDMTools 

%description
The Climate Prediction Center's (CPC) rainfall data for the world (1979 to
present, 50 km resolution) and the USA (1948 to present, 25 km
resolution), is one of the few high quality, long term, observation based,
daily rainfall products available for free. Although raw data is available
at CPC's ftp site, obtaining, processing and visualizing the data is not
straightforward. There are more than 12,000 files for the world and about
24,000 files for the USA. Moreover, file formats and file extensions have
not been consistent. This package provides functionality to download,
process and visualize over 35 years of global rainfall data and over 65
years of USA rainfall data from CPC.

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
