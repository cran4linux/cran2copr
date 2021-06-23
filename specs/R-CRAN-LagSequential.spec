%global __brp_check_rpaths %{nil}
%global packname  LagSequential
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Lag-Sequential Categorical Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.0
Requires:         R-core >= 1.9.0
BuildArch:        noarch

%description
Lag-sequential analysis is a method of assessing of patterns (what tends
to follow what?) in sequences of codes. The codes are typically for
discrete behaviors or states. The functions in this package read a stream
of codes, or a frequency transition matrix, and produce a variety of lag
sequential statistics, including transitional frequencies, expected
transitional frequencies, transitional probabilities, z values, adjusted
residuals, Yule's Q values, likelihood ratio tests of stationarity across
time and homogeneity across groups or segments, transformed kappas for
unidirectional dependence, bidirectional dependence, parallel and
nonparallel dominance, and significance levels based on both parametric
and randomization tests. The methods are described in Bakeman & Quera
(2011) <doi:10.1017/CBO9781139017343>, O'Connor (1999)
<doi:10.3758/BF03200753>, Wampold & Margolin (1982)
<doi:10.1037/0033-2909.92.3.755>, and Wampold (1995, ISBN:0-89391-919-5).

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
