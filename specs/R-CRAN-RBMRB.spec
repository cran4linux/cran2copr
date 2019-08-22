%global packname  RBMRB
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}
Summary:          BMRB Data Access and Visualization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.5.6
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-rjson >= 0.2.15
BuildRequires:    R-stats 
Requires:         R-CRAN-plotly >= 4.5.6
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-rjson >= 0.2.15
Requires:         R-stats 

%description
The Biological Magnetic Resonance Data Bank (BMRB,<http://
www.bmrb.wisc.edu/>) collects, annotates, archives, and disseminates
(worldwide in the public domain) the important spectral and quantitative
data derived from NMR(Nuclear Magnetic Resonance) spectroscopic
investigations of biological macromolecules and metabolites. This package
provides an interface to BMRB database for easy data access and includes a
minimal set of data visualization functions. Users are encouraged to make
their own data visualizations using BMRB data.

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
