%global packname  APtools
%global packver   6.8.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.8.8
Release:          1%{?dist}
Summary:          Average Positive Predictive Values (AP) for Binary Outcomes andCensored Event Times

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-cmprsk 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-survival 
Requires:         R-CRAN-cmprsk 

%description
We provide tools to estimate two prediction accuracy metrics, the average
positive predictive values (AP) as well as the well-known AUC (the area
under the receiver operator characteristic curve) for risk scores. The
outcome of interest is either binary or censored event time. Note that for
censored event time, our functions' estimates, the AP and the AUC, are
time-dependent for pre-specified time interval(s). A function that
compares the APs of two risk scores/markers is also included. Optional
outputs include positive predictive values and true positive fractions at
the specified marker cut-off values, and a plot of the time-dependent AP
versus time (available for event time data).

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
