%global packname  kst
%global packver   0.5-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          2%{?dist}
Summary:          Knowledge Space Theory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sets >= 1.0.17
BuildRequires:    R-CRAN-relations >= 0.6.7
BuildRequires:    R-CRAN-proxy 
Requires:         R-CRAN-sets >= 1.0.17
Requires:         R-CRAN-relations >= 0.6.7
Requires:         R-CRAN-proxy 

%description
Knowledge space theory by Doignon and Falmagne (1999)
<doi:10.1007/978-3-642-58625-5> is a set- and order-theoretical framework,
which proposes mathematical formalisms to operationalize knowledge
structures in a particular domain. The 'kst' package provides basic
functionalities to generate, handle, and manipulate knowledge structures
and knowledge spaces.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
