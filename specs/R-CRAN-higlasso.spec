%global packname  higlasso
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}
Summary:          Hierarchical Integrative Group LASSO

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-gcdnet 
BuildRequires:    R-CRAN-gglasso 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-gcdnet 
Requires:         R-CRAN-gglasso 
Requires:         R-CRAN-purrr 
Requires:         R-splines 
Requires:         R-CRAN-Rcpp 

%description
Environmental health studies are increasingly measuring multiple
pollutants to characterize the joint health effects attributable to
exposure mixtures. However, the underlying dose-response relationship
between toxicants and health outcomes of interest may be highly nonlinear,
with possible nonlinear interaction effects. Hierarchical integrative
group least absolute shrinkage and selection operator (HiGLASSO),
developed by Boss et al (2020) <arXiv:2003.12844>, is a general framework
to identify noteworthy nonlinear main and interaction effects in the
presence of group structures among a set of exposures.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
