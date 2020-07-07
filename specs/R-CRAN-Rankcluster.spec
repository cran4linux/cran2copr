%global packname  Rankcluster
%global packver   0.94.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.94.2
Release:          3%{?dist}
Summary:          Model-Based Clustering for Multivariate Partial Ranking Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Implementation of a model-based clustering algorithm for ranking data (C.
Biernacki, J. Jacques (2013) <doi:10.1016/j.csda.2012.08.008>).
Multivariate rankings as well as partial rankings are taken into account.
This algorithm is based on an extension of the Insertion Sorting Rank
(ISR) model for ranking data, which is a meaningful and effective model
parametrized by a position parameter (the modal ranking, quoted by mu) and
a dispersion parameter (quoted by pi). The heterogeneity of the rank
population is modelled by a mixture of ISR, whereas conditional
independence assumption is considered for multivariate rankings.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
