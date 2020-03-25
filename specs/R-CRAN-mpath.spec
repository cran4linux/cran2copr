%global packname  mpath
%global packver   0.3-24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.24
Release:          1%{?dist}
Summary:          Regularized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-bst 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-bst 

%description
Algorithms optimize penalized models. Currently the models include
penalized Poisson, negative binomial, zero-inflated Poisson, zero-inflated
negative binomial regression models and robust models. The penalties
include least absolute shrinkage and selection operator (LASSO), smoothly
clipped absolute deviation (SCAD), minimax concave penalty (MCP), and each
possibly combining with L_2 penalty. See Wang et al. (2014)
<doi:10.1002/sim.6314>, Wang et al. (2015) <doi:10.1002/bimj.201400143>,
Wang et al. (2016) <doi:10.1177/0962280214530608>, Wang (2019)
<arXiv:1912.11119>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
