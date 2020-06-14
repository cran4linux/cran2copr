%global packname  BDgraph
%global packver   2.62
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.62
Release:          2%{?dist}
Summary:          Bayesian Structure Learning in Graphical Models usingBirth-Death MCMC

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
Statistical tools for Bayesian structure learning in undirected graphical
models for continuous, discrete, and mixed data. The package is
implemented the recent improvements in the Bayesian graphical models
literature, including Mohammadi and Wit (2015) <doi:10.1214/14-BA889>,
Mohammadi and Wit (2019) <doi:10.18637/jss.v089.i03>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
