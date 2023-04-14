%global __brp_check_rpaths %{nil}
%global packname  G2Sd
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Grain-Size Statistics and Description of Sediment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-xlsxjars 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-xlsxjars 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Full descriptive statistics, physical description of sediment, metric or
phi sieves.

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
