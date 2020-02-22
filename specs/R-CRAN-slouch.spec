%global packname  slouch
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          1%{?dist}
Summary:          Stochastic Linear Ornstein-Uhlenbeck Comparative Hypotheses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-memoise 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-crayon 
Requires:         R-parallel 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-memoise 

%description
An implementation of a phylogenetic comparative method. It can fit
univariate among-species Ornstein-Uhlenbeck models of phenotypic trait
evolution, where the trait evolves towards a primary optimum. The optimum
can be modelled as a single parameter, as multiple discrete regimes on the
phylogenetic tree, and/or with continuous covariates. See also Hansen
(1997) <doi:10.2307/2411186>, Butler & King (2004) <doi:10.1086/426002>,
Hansen et al. (2008) <doi:10.1111/j.1558-5646.2008.00412.x>.

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
