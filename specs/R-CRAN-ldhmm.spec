%global __brp_check_rpaths %{nil}
%global packname  ldhmm
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Hidden Markov Model for Financial Time-Series Based on LambdaDistribution

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xts >= 0.10.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ecd 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
Requires:         R-CRAN-xts >= 0.10.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ecd 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-moments 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-methods 

%description
Hidden Markov Model (HMM) based on symmetric lambda distribution framework
is implemented for the study of return time-series in the financial
market. Major features in the S&P500 index, such as regime identification,
volatility clustering, and anti-correlation between return and volatility,
can be extracted from HMM cleanly. Univariate symmetric lambda
distribution is essentially a location-scale family of exponential power
distribution. Such distribution is suitable for describing highly
leptokurtic time series obtained from the financial market. It provides a
theoretically solid foundation to explore such data where the normal
distribution is not adequate. The HMM implementation follows closely the
book: "Hidden Markov Models for Time Series", by Zucchini, MacDonald,
Langrock (2016).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
