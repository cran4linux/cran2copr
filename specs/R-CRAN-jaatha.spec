%global packname  jaatha
%global packver   3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Simulation-Based Maximum Likelihood Parameter Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.1.1
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.1.1
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
An estimation method that can use computer simulations to approximate
maximum-likelihood estimates even when the likelihood function can not be
evaluated directly. It can be applied whenever it is feasible to conduct
many simulations, but works best when the data is approximately Poisson
distributed. It was originally designed for demographic inference in
evolutionary biology. It has optional support for conducting coalescent
simulation using the 'coala' package.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
