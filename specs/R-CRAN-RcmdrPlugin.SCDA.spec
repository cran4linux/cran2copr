%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.SCDA
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Rcmdr Plugin for Designing and Analyzing Single-Case Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SCVA 
BuildRequires:    R-CRAN-SCRT 
BuildRequires:    R-CRAN-SCMA 
BuildRequires:    R-CRAN-Rcmdr 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-SCVA 
Requires:         R-CRAN-SCRT 
Requires:         R-CRAN-SCMA 
Requires:         R-CRAN-Rcmdr 
Requires:         R-tcltk 

%description
Provides a GUI for the SCVA, SCRT and SCMA packages as described in Bulte
and Onghena (2013) <doi:10.22237/jmasm/1383280020>. The package is written
as an Rcmdr plugin.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
