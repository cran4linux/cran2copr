%global packname  FarmTest
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Factor Adjusted Robust Multiple Testing

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 

%description
Performs robust multiple testing for means in the presence of known and
unknown latent factors. It implements a robust procedure to estimate
distribution parameters using the Huber's loss function and accounts for
strong dependence among coordinates via an approximate factor model. This
method is particularly suitable for high dimensional data when there are
many variables but only a small number of observations available.
Moreover, the method is tailored to cases when the underlying distribution
deviates from Gaussian, which is commonly assumed in the literature.
Besides the results of hypotheses testing, the estimated underlying
factors and diagnostic plots are also output. Multiple comparison
correction is done after estimating the proportion of true null hypotheses
using the method in Storey (2015) <https://github.com/jdstorey/qvalue>.
For detailed description of methods and further references, see the papers
on the 'FarmTest' method: Fan et al. (2017) <arXiv:1711.05386> and Zhou et
al. (2017) <arXiv:1711.05381>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
