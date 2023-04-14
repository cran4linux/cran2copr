%global __brp_check_rpaths %{nil}
%global packname  censusr
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Collect Data from the Census API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-stringr 

%description
Use the US Census API to collect summary data tables for SF1 and ACS
datasets at arbitrary geographies.

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
