%global packname  sBIC
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Computing the Singular BIC for Multiple Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R.oo >= 1.20.0
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-poLCA 
BuildRequires:    R-CRAN-R.methodsS3 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-hash 
Requires:         R-CRAN-R.oo >= 1.20.0
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-poLCA 
Requires:         R-CRAN-R.methodsS3 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-hash 

%description
Computes the sBIC for various singular model collections including:
binomial mixtures, factor analysis models, Gaussian mixtures, latent
forests, latent class analyses, and reduced rank regressions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
