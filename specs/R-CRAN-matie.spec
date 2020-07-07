%global packname  matie
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Measuring Association and Testing Independence Efficiently

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-cba 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-seriation 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-cba 

%description
Uses a ratio of weighted distributions to estimate association between
variables in a data set.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
