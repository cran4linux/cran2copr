%global packname  CMF
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Collective Matrix Factorization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Collective matrix factorization (CMF) finds joint low-rank representations
for a collection of matrices with shared row or column entities. This code
learns a variational Bayesian approximation for CMF, supporting multiple
likelihood potentials and missing data, while identifying both factors
shared by multiple matrices and factors private for each matrix. For
further details on the method see Klami et al. (2014) <arXiv:1312.5921>.
The package can also be used to learn Bayesian canonical correlation
analysis (CCA) and group factor analysis (GFA) models, both of which are
special cases of CMF. This is likely to be useful for people looking for
CCA and GFA solutions supporting missing data and non-Gaussian
likelihoods. See Klami et al. (2013)
<http://www.jmlr.org/papers/v14/klami13a.html> and Virtanen et al. (2012)
<http://proceedings.mlr.press/v22/virtanen12.html> for details on Bayesian
CCA and GFA, respectively.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
