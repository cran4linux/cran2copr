%global packname  FishResp
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Analytical Tool for Aquatic Respirometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-rMR 
BuildRequires:    R-CRAN-respirometry 
Requires:         R-CRAN-chron 
Requires:         R-lattice 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-rMR 
Requires:         R-CRAN-respirometry 

%description
Calculates metabolic rate of fish and other aquatic organisms measured
using an intermittent-flow respirometry approach. The tool is used to run
a set of graphical QC tests of raw respirometry data, correct it for
background respiration and chamber effect, filter and extract target
values of absolute and mass-specific metabolic rate. Experimental design
should include background respiration tests and measuring of one or more
metabolic rate traits. The package allows a user to import raw
respirometry data obtained from 'AquaResp' (free software), 'AutoResp'
('LoligoSystems'), 'OxyView' ('PreSens'), 'Pyro Oxygen Logger'
('PyroScience') and 'Q-box Aqua' ('QubitSystems').

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
