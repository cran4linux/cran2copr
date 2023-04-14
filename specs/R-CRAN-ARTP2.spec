%global __brp_check_rpaths %{nil}
%global packname  ARTP2
%global packver   0.9.45
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.45
Release:          3%{?dist}%{?buildtag}
Summary:          Pathway and Gene-Level Association Test

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-parallel 
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Formula 
Requires:         R-parallel 

%description
Pathway and gene level association test using raw data or summary
statistics.

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
