%global packname  JFE
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}
Summary:          Tools and GUI for Analyzing Data of Just Finance andEconometrics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-fPortfolio 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-BurStFin 
BuildRequires:    R-CRAN-fAssets 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-FRAPO 
BuildRequires:    R-CRAN-iClick 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-fPortfolio 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-BurStFin 
Requires:         R-CRAN-fAssets 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-FRAPO 
Requires:         R-CRAN-iClick 
Requires:         R-MASS 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-rugarch 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-zoo 

%description
Support the analysis of global assets selection and portfolio backtesting,
we also enhance the computation of some performance ratios of
'PerformanceAnalytics'.

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
