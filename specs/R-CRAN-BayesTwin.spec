%global packname  BayesTwin
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Item-Level Twin Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-rjags 
Requires:         R-foreign 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-rjags 

%description
Bayesian analysis of item-level hierarchical twin data using an integrated
item response theory model. Analyses are based on Schwabe & van den Berg
(2014) <doi:10.1007/s10519-014-9649-7>, Molenaar & Dolan (2014)
<doi:10.1007/s10519-014-9647-9>, Schwabe, Jonker & van den Berg (2016)
<doi:10.1007/s10519-015-9768-9> and Schwabe, Boomsma & van den Berg (2016)
<doi:10.1016/j.lindif.2017.01.018>.

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
