%global packname  extRemes
%global packver   2.0-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.11
Release:          1%{?dist}
Summary:          Extreme Value Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-distillery >= 1.0.4
BuildRequires:    R-CRAN-Lmoments 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-distillery >= 1.0.4
Requires:         R-CRAN-Lmoments 
Requires:         R-graphics 
Requires:         R-stats 

%description
Functions for performing extreme value analysis.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
