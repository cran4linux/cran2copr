%global packname  machQA
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          QA Machina Indicators

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-machina 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-machina 
Requires:         R-CRAN-plyr 

%description
Performs Quality Analysis on Machina algebraic indicators 'sma' (simple
moving average), 'wavg' (weighted average),'xavg' (exponential moving
average), 'hma' (Hull moving average), 'adma' (adaptive moving average),
'tsi' (true strength index), 'rsi' (relative strength index), 'gauss'
(Gaussian elimination), 'momo' (momentum), 't3' (triple exponential moving
average), 'macd' (moving average convergence divergence). Machina is a
strategy creation and backtesting engine for quants and financial
professionals (see <https://machi.na/> for more information).

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
%doc %{rlibdir}/%{packname}/base_files
%doc %{rlibdir}/%{packname}/TS_files
%{rlibdir}/%{packname}/INDEX
