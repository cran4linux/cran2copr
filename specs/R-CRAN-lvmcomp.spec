%global __brp_check_rpaths %{nil}
%global packname  lvmcomp
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic EM Algorithms for Latent Variable Models with aHigh-Dimensional Latent Space

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-coda >= 0.19.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-coda >= 0.19.1
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-stats 

%description
Provides stochastic EM algorithms for latent variable models with a
high-dimensional latent space. So far, we provide functions for
confirmatory item factor analysis based on the multidimensional two
parameter logistic (M2PL) model and the generalized multidimensional
partial credit model. These functions scale well for problems with many
latent traits (e.g., thirty or even more) and are virtually tuning-free.
The computation is facilitated by multiprocessing 'OpenMP' API. For more
information, please refer to: Zhang, S., Chen, Y., & Liu, Y. (2018). An
Improved Stochastic EM Algorithm for Large-scale Full-information Item
Factor Analysis. British Journal of Mathematical and Statistical
Psychology. <doi:10.1111/bmsp.12153>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
