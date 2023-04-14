%global __brp_check_rpaths %{nil}
%global packname  Compack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Regression with Compositional Covariates

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-orthogonalsplinebasis 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-MASS 
Requires:         R-CRAN-plyr 
Requires:         R-splines 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-orthogonalsplinebasis 
Requires:         R-methods 

%description
Regression methodologies with compositional covariates, including (1)
sparse log-contrast regression with compositional covariates proposed by
Lin et al. (2014) <doi:10.1093/biomet/asu031>, and (2) sparse log-contrast
regression with functional compositional predictors proposed by Sun et al.
(2020) <arXiv:1808.02403>.

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
%{rlibdir}/%{packname}
