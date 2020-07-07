%global packname  imbalance
%global packver   1.0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.1
Release:          3%{?dist}
Summary:          Preprocessing Algorithms for Imbalanced Datasets

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-KernelKnn 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-smotefamily 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-KernelKnn 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-smotefamily 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-C50 

%description
Class imbalance usually damages the performance of classifiers. Thus, it
is important to treat data before applying a classifier algorithm. This
package includes recent resampling algorithms in the literature: (Barua et
al. 2014) <doi:10.1109/tkde.2012.232>; (Das et al. 2015)
<doi:10.1109/tkde.2014.2324567>, (Zhang et al. 2014)
<doi:10.1016/j.inffus.2013.12.003>; (Gao et al. 2014)
<doi:10.1016/j.neucom.2014.02.006>; (Almogahed et al. 2014)
<doi:10.1007/s00500-014-1484-5>. It also includes an useful interface to
perform oversampling.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
