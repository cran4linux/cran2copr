%global __brp_check_rpaths %{nil}
%global packname  diverse
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Diversity Measures for Complex Systems

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-foreign 
BuildRequires:    R-stats 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-reshape2 
Requires:         R-foreign 
Requires:         R-stats 

%description
Computes the most common diversity measures used in social and other
sciences, and includes new measures from interdisciplinary research.

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
