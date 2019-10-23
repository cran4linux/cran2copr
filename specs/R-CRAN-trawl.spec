%global packname  trawl
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Estimation and Simulation of Trawl Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-Runuran 
BuildRequires:    R-CRAN-squash 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TSA 
Requires:         R-CRAN-DEoptim 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-Runuran 
Requires:         R-CRAN-squash 
Requires:         R-stats 
Requires:         R-CRAN-TSA 

%description
Contains R functions for simulating and estimating integer-valued trawl
processes as described in the article "Modelling, simulation and inference
for multivariate time series of counts using trawl processes" by A. E. D.
Veraart (Journal of Multivariate Analysis, 2018, to appear, preprint
available at:
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3100076> ) and for
simulating random vectors from the bivariate negative binomial and the bi-
and trivariate logarithmic series distributions.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
