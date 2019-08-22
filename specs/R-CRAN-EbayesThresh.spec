%global packname  EbayesThresh
%global packver   1.4-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.12
Release:          1%{?dist}
Summary:          Empirical Bayes Thresholding and Related Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wavethresh 
Requires:         R-stats 
Requires:         R-CRAN-wavethresh 

%description
Empirical Bayes thresholding using the methods developed by I. M.
Johnstone and B. W. Silverman. The basic problem is to estimate a mean
vector given a vector of observations of the mean vector plus white noise,
taking advantage of possible sparsity in the mean vector. Within a
Bayesian formulation, the elements of the mean vector are modelled as
having, independently, a distribution that is a mixture of an atom of
probability at zero and a suitable heavy-tailed distribution. The mixing
parameter can be estimated by a marginal maximum likelihood approach. This
leads to an adaptive thresholding approach on the original data.
Extensions of the basic method, in particular to wavelet thresholding, are
also implemented within the package.

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
%doc %{rlibdir}/%{packname}/kan-xu-thesis.pdf
%{rlibdir}/%{packname}/INDEX
