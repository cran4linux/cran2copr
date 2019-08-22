%global packname  bayesImageS
%global packver   0.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Bayesian Methods for Image Segmentation using a Potts Model

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.10.6

%description
Various algorithms for segmentation of 2D and 3D images, such as computed
tomography and satellite remote sensing. This package implements Bayesian
image analysis using the hidden Potts model with external field prior of
Moores et al. (2015) <doi:10.1016/j.csda.2014.12.001>. Latent labels are
sampled using chequerboard updating or Swendsen-Wang. Algorithms for the
smoothing parameter include pseudolikelihood, path sampling, the exchange
algorithm, approximate Bayesian computation (ABC-MCMC and ABC-SMC), and
the parametric functional approximate Bayesian (PFAB) algorithm. Refer to
<doi:10.1007/s11222-014-9525-6> and <doi:10.1214/18-BA1130> for further
details.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/image
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
