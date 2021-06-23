%global __brp_check_rpaths %{nil}
%global packname  SGB
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Simplicial Generalized Beta Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-alabama 
Requires:         R-CRAN-Formula 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-alabama 

%description
Main properties and regression procedures using a generalization of the
Dirichlet distribution called Simplicial Generalized Beta distribution. It
is a new distribution on the simplex (i.e. on the space of compositions or
positive vectors with sum of components equal to 1). The Dirichlet
distribution can be constructed from a random vector of independent Gamma
variables divided by their sum. The SGB follows the same construction with
generalized Gamma instead of Gamma variables. The Dirichlet exponents are
supplemented by an overall shape parameter and a vector of scales. The
scale vector is itself a composition and can be modeled with auxiliary
variables through a log-ratio transformation. Graf, M. (2017, ISBN:
978-84-947240-0-8). See also the vignette enclosed in the package.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
