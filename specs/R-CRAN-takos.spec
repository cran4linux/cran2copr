%global packname  takos
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Differential Calorimetry Scans

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-devEMF 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-smoother 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-baseline 
BuildRequires:    R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-devEMF 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-smoother 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-minpack.lm 
Requires:         R-tools 
Requires:         R-CRAN-baseline 
Requires:         R-graphics 

%description
It includes functions for applying methodologies utilized for
single-process kinetic analysis of solid-state processes were recently
summarized and described in the Recommendation of ICTAC Kinetic Committee.
These methods work with the basic kinetic equation. The Methodologies
included refers to Avrami, Friedman, Kissinger, Ozawa, OFM, Mo, Starink,
isoconversional methodology (Vyazovkin) according to ICATAC Kinetics
Committee recommendations as reported in Vyazovkin S, Chrissafis K, Di
Lorenzo ML, et al. ICTAC Kinetics Committee recommendations for collecting
experimental thermal analysis data for kinetic computations. Thermochim
Acta. 2014;590:1-23. <doi:10.1016/J.TCA.2014.05.036> .

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
