%global packname  iClick
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          A Button-Based GUI for Financial and Economic Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-coefplot 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-papeR 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-zoo 
Requires:         R-lattice 
Requires:         R-CRAN-rugarch 
Requires:         R-tcltk 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-xts 
Requires:         R-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-coefplot 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-forecast 
Requires:         R-grid 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-papeR 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-zoo 

%description
A GUI designed to support the analysis of financial-economic time series
data.

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
