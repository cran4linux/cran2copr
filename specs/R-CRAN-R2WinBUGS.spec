%global packname  R2WinBUGS
%global packver   2.1-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.21
Release:          3%{?dist}%{?buildtag}
Summary:          Running 'WinBUGS' and 'OpenBUGS' from 'R' / 'S-PLUS'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda >= 0.11.0
BuildRequires:    R-boot 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-coda >= 0.11.0
Requires:         R-boot 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 

%description
Invoke a 'BUGS' model in 'OpenBUGS' or 'WinBUGS', a class "bugs" for
'BUGS' results and functions to work with that class. Function
write.model() allows a 'BUGS' model file to be written. The class and
auxiliary functions could be used with other MCMC programs, including
'JAGS'.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/model
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
