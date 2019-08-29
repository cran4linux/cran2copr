%global packname  Biograph
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          1%{?dist}
Summary:          Explore Life Histories

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvna 
BuildRequires:    R-CRAN-etm 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-mstate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvna 
Requires:         R-CRAN-etm 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-Epi 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-plyr 
Requires:         R-survival 
Requires:         R-CRAN-mstate 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Transition rates are computed from transitions and exposures.Useful
graphics and life-course indicators are computed. The package structures
the data for multistate statistical and demographic modeling of life
histories.

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
%doc %{rlibdir}/%{packname}/Doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
