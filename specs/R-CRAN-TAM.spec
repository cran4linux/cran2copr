%global packname  TAM
%global packver   3.5-19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.19
Release:          2%{?dist}
Summary:          Test Analysis Modules

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-CDM >= 6.4.19
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CDM >= 6.4.19
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Includes marginal maximum likelihood estimation and joint maximum
likelihood estimation for unidimensional and multidimensional item
response models. The package functionality covers the Rasch model, 2PL
model, 3PL model, generalized partial credit model, multi-faceted Rasch
model, nominal item response model, structured latent class model, mixture
distribution IRT models, and located latent class models. Latent
regression models and plausible value imputation are also supported. For
details see Adams, Wilson and Wang, 1997 <doi:10.1177/0146621697211001>,
Adams, Wilson and Wu, 1997 <doi:10.3102/10769986022001047>, Formann, 1982
<doi:10.1002/bimj.4710240209>, Formann, 1992
<doi:10.1080/01621459.1992.10475229>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
