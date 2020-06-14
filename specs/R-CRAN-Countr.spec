%global packname  Countr
%global packver   3.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.4
Release:          2%{?dist}
Summary:          Flexible Univariate Count Models Based on Renewal Processes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rdpack >= 0.7.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-utils 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-standardize 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rdpack >= 0.7.0
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-Matrix 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-numDeriv 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-CRAN-car 
Requires:         R-utils 
Requires:         R-lattice 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-standardize 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-xtable 

%description
Flexible univariate count models based on renewal processes. The models
may include covariates and can be specified with familiar formula syntax
as in glm() and package 'flexsurv'. The methodology is described in a
forthcoming paper in the Journal of Statistical Software
<10.18637/jss.v090.i13> (included as vignette 'Countr_guide' in the
package).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
