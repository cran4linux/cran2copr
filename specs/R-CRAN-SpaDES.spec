%global packname  SpaDES
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          2%{?dist}
Summary:          Develop and Run Spatially Explicit Discrete Event SimulationModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quickPlot 
BuildRequires:    R-CRAN-reproducible 
BuildRequires:    R-CRAN-SpaDES.addins 
BuildRequires:    R-CRAN-SpaDES.core 
BuildRequires:    R-CRAN-SpaDES.tools 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-quickPlot 
Requires:         R-CRAN-reproducible 
Requires:         R-CRAN-SpaDES.addins 
Requires:         R-CRAN-SpaDES.core 
Requires:         R-CRAN-SpaDES.tools 
Requires:         R-utils 

%description
Metapackage for implementing a variety of event-based models, with a focus
on spatially explicit models. These include raster-based, event-based, and
agent-based models. The core simulation components (provided by
'SpaDES.core') are built upon a discrete event simulation (DES; see
Matloff (2011) ch 7.8.3 <https://nostarch.com/artofr.htm>) framework that
facilitates modularity, and easily enables the user to include additional
functionality by running user-built simulation modules (see also
'SpaDES.tools'). Included are numerous tools to visualize rasters and
other maps (via 'quickPlot'), and caching methods for reproducible
simulations (via 'reproducible'). Additional functionality is provided by
the 'SpaDES.addins' and 'SpaDES.shiny' packages.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
