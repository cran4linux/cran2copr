%global packname  glmBfp
%global packver   0.0-51
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.51
Release:          1%{?dist}
Summary:          Bayesian Fractional Polynomials for GLMs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildRequires:    R-CRAN-Runuran >= 0.12
BuildRequires:    R-CRAN-Rcpp >= 0.11.6
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Runuran >= 0.12
Requires:         R-CRAN-Rcpp >= 0.11.6
Requires:         R-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-statmod 
Requires:         R-methods 
Requires:         R-CRAN-coda 

%description
Implements the Bayesian paradigm for fractional polynomials in generalized
linear models, described by Held, Gravestock, Sabanes Bove (2015)
<doi:10.1214/14-STS510>. See package 'bfp' for the treatment of normal
models.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
