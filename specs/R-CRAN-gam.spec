%global packname  gam
%global packver   1.16.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.16.1
Release:          1%{?dist}
Summary:          Generalized Additive Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-CRAN-foreach 

%description
Functions for fitting and working with generalized additive models, as
described in chapter 7 of "Statistical Models in S" (Chambers and Hastie
(eds), 1991), and "Generalized Additive Models" (Hastie and Tibshirani,
1990).

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
%doc %{rlibdir}/%{packname}/ratfor
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
