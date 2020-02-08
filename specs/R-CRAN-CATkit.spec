%global packname  CATkit
%global packver   3.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.3
Release:          1%{?dist}
Summary:          Chronomics Analysis Toolkit (CAT): Periodicity Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-rtf 
BuildRequires:    R-CRAN-season 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-assertr 
BuildRequires:    R-CRAN-CombMSC 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-MASS 
Requires:         R-CRAN-png 
Requires:         R-CRAN-rtf 
Requires:         R-CRAN-season 
Requires:         R-CRAN-magic 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-assertr 
Requires:         R-CRAN-CombMSC 
Requires:         R-CRAN-Hmisc 

%description
Calculates auto- and cross-correlation functions and plots an actogram and
a smoothing function from a time series to identify and visualize periodic
components. Tests presence of anticipated rhythm and estimates rhythm
parameters; fits model consisting of multiple rhythmic components to data;
performs least squares spectral analysis and other cosinor-based analyses,
including population-mean cosinor (PMC) and population-mean cosinor
parameter tests (PMCtest).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/pngFiles
%{rlibdir}/%{packname}/INDEX
