%global packname  MultipleBubbles
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Test and Detection of Explosive Behaviors for Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-stats 
Requires:         R-MASS >= 7.3
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-stats 

%description
Provides the Augmented Dickey-Fuller test and its variations to check the
existence of bubbles (explosive behavior) for time series, based on the
article by Peter C. B. Phillips, Shuping Shi and Jun Yu (2015a)
<doi:10.1111/iere.12131>. Some functions may take a while depending on the
size of the data used, or the number of Monte Carlo replications applied.

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
