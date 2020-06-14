%global packname  spgwr
%global packver   0.6-33
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.33
Release:          2%{?dist}
Summary:          Geographically Weighted Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-sp >= 0.8.3
BuildRequires:    R-CRAN-spData >= 0.2.6.2
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp >= 0.8.3
Requires:         R-CRAN-spData >= 0.2.6.2
Requires:         R-stats 
Requires:         R-methods 

%description
Functions for computing geographically weighted regressions are provided,
based on work by Chris Brunsdon, Martin Charlton and Stewart Fotheringham.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/backstore
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shapes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
