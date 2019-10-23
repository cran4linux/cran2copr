%global packname  streamMOA
%global packver   1.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Interface for MOA Stream Clustering Algorithms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stream >= 1.1.2
BuildRequires:    R-CRAN-rJava >= 0.9.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-stream >= 1.1.2
Requires:         R-CRAN-rJava >= 0.9.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Interface for data stream clustering algorithms implemented in the MOA
(Massive Online Analysis) framework (Albert Bifet, Geoff Holmes, Richard
Kirkby, Bernhard Pfahringer (2010). MOA: Massive Online Analysis, Journal
of Machine Learning Research 11: 1601-1604).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
