%global packname  coprimary
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Sample Size Calculation for Two Primary Time-to-Event Endpointsin Clinical Trials

License:          GPL (>= 3.3.2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gsDesign 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-proto 
Requires:         R-stats 
Requires:         R-CRAN-gsDesign 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-proto 

%description
Computes the required number of patients for two time-to-event end-points
as primary endpoint in phase III clinical trial.

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
