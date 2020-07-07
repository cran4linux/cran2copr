%global packname  BMTME
%global packver   1.0.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.15
Release:          3%{?dist}
Summary:          Bayesian Multi-Trait Multi-Environment for Genomic SelectionAnalysis

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-BGLR 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-BGLR 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-tidyr 

%description
Genomic selection and prediction models with the capacity to use multiple
traits and environments, through ready-to-use Bayesian models. It consists
a group of functions that help to create regression models for some
genomic models proposed by Montesinos-López, et al. (2016)
<doi:10.1534/g3.116.032359> also in Montesinos-López et al. (2018)
<doi:10.1534/g3.118.200728> and Montesinos-López et al. (2018)
<doi:10.2134/agronj2018.06.0362>.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
