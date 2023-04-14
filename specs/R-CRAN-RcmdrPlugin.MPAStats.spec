%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.MPAStats
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          R Commander Plug-in for MPA Statistics

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.4.0
BuildRequires:    R-CRAN-ordinal 
Requires:         R-CRAN-Rcmdr >= 1.4.0
Requires:         R-CRAN-ordinal 

%description
Extends R Commander with a unified menu of new and pre-existing
statistical functions related to public management and policy analysis
statistics. Functions and menus have been renamed according to the usage
in PMGT 630 in the Master of Public Administration program at Brigham
Young University.

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
