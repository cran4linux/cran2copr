%global packname  longitudinalcascade
%global packver   0.3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2.1
Release:          3%{?dist}
Summary:          Longitudinal Cascade

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lubridate 

%description
Creates a series of set of graphics and statistics related to the
longitudinal cascade, all included in a single object. The longitudinal
cascade inputs longitudinal data to identify gaps in the HIV and related
cascades by observing differences using time to event and survival
methods. The stage definitions are set by the user, with default standard
options. Outputs include graphics, datasets, and formal statistical tests.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
