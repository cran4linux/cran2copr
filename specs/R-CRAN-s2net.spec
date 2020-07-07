%global packname  s2net
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          The Generalized Semi-Supervised Elastic-Net

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-MASS 

%description
Implements the generalized semi-supervised elastic-net. This method
extends the supervised elastic-net problem, and thus it is a practical
solution to the problem of feature selection in semi-supervised contexts.
Its mathematical formulation is presented from a general perspective,
covering a wide range of models.  We focus on linear and logistic
responses, but the implementation could be easily extended to other losses
in generalized linear models. We develop a flexible and fast
implementation, written in 'C++' using 'RcppArmadillo' and integrated into
R via 'Rcpp' modules. See Culp, M. 2013 <doi:10.1080/10618600.2012.657139>
for references on the Joint Trained Elastic-Net.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
