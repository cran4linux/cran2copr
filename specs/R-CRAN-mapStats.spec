%global packname  mapStats
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Geographic Display of Survey Data Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-survey 
Requires:         R-lattice 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-reshape2 

%description
Automated calculation and visualization of survey data statistics on a
color-coded map.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/shapes
%{rlibdir}/%{packname}/INDEX
