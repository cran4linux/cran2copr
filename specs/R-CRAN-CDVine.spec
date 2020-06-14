%global packname  CDVine
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          2%{?dist}
Summary:          Statistical Inference of C- And D-Vine Copulas

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-stats 

%description
Functions for statistical inference of canonical vine (C-vine) and D-vine
copulas. Tools for bivariate exploratory data analysis and for bivariate
as well as vine copula selection are provided. Models can be estimated
either sequentially or by joint maximum likelihood estimation. Sampling
algorithms and plotting methods are also included. Data is assumed to lie
in the unit hypercube (so-called copula data).

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
