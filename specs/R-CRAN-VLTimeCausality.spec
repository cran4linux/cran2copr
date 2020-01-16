%global packname  VLTimeCausality
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Variable-Lag Time Series Causality Inference Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-RTransferEntropy 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-RTransferEntropy 

%description
A framework to infer causality on a pair of time series of real numbers
based on variable-lag Granger causality and transfer entropy. Typically,
Granger causality and transfer entropy have an assumption of a fixed and
constant time delay between the cause and effect. However, for a
non-stationary time series, this assumption is not true. For example,
considering two time series of velocity of person A and person B where B
follows A. At some time, B stops tying his shoes, then running to catch up
A. The fixed-lag assumption is not true in this case. We propose a
framework that allows variable-lags between cause and effect in Granger
causality and transfer entropy to allow them to deal with variable-lag
non-stationary time series. Please see Chainarong Amornbunchornvej, Elena
Zheleva, and Tanya Berger-Wolf (2019)
<https://www.cs.uic.edu/~elena/pubs/amornbunchornvej-dsaa19.pdf> when
referring to this package in publications.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/VLTimeCausality_0.1.0.pdf
%{rlibdir}/%{packname}/INDEX
