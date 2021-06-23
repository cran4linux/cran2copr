%global __brp_check_rpaths %{nil}
%global packname  distrEx
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          3%{?dist}%{?buildtag}
Summary:          Extensions of Package 'distr'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-distr >= 2.8.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-startupmsg 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-distr >= 2.8.0
Requires:         R-methods 
Requires:         R-CRAN-startupmsg 
Requires:         R-utils 
Requires:         R-stats 

%description
Extends package 'distr' by functionals, distances, and conditional
distributions.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/MASKING
%doc %{rlibdir}/%{packname}/MOVED
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
