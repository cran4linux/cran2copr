%global __brp_check_rpaths %{nil}
%global packname  processmonitR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Building Process Monitoring Dashboards

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-bupaR 
BuildRequires:    R-CRAN-edeaR 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-bupaR 
Requires:         R-CRAN-edeaR 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 

%description
Functions for constructing dashboards for business process monitoring.
Building on the event log objects class from package 'bupaR'. Allows the
use to assemble custom shiny dashboards based on process data.

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
