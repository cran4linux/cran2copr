%global packname  abcrf
%global packver   1.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.1
Release:          3%{?dist}
Summary:          Approximate Bayesian Computation via Random Forests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-readr 
Requires:         R-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 

%description
Performs Approximate Bayesian Computation (ABC) model choice and parameter
inference via random forests. Pudlo P., Marin J.-M., Estoup A., Cornuet
J.-M., Gautier M. and Robert C. P. (2016)
<doi:10.1093/bioinformatics/btv684>. Estoup A., Raynal L., Verdu P. and
Marin J.-M. <http://journal-sfds.fr/article/view/709>. Raynal L., Marin
J.-M., Pudlo P., Ribatet M., Robert C. P. and Estoup A. (2019)
<doi:10.1093/bioinformatics/bty867>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
