%global __brp_check_rpaths %{nil}
%global packname  drc
%global packver   3.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Dose-Response Curves

License:          GPL-2 | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-scales 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-scales 

%description
Analysis of dose-response data is made available through a suite of
flexible and versatile model fitting and after-fitting functions.

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
