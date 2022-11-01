%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mtlgmm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unsupervised Multi-Task and Transfer Learning on Gaussian Mixture Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-mclust 
Requires:         R-stats 

%description
Unsupervised learning has been widely used in many real-world
applications. One of the simplest and most important unsupervised learning
models is the Gaussian mixture model (GMM). In this work, we study the
multi-task learning problem on GMMs, which aims to leverage potentially
similar GMM parameter structures among tasks to obtain improved learning
performance compared to single-task learning. We propose a multi-task GMM
learning procedure based on the Expectation-Maximization (EM) algorithm
that not only can effectively utilize unknown similarity between related
tasks but is also robust against a fraction of outlier tasks from
arbitrary sources. The proposed procedure is shown to achieve minimax
optimal rate of convergence for both parameter estimation error and the
excess mis-clustering error, in a wide range of regimes. Moreover, we
generalize our approach to tackle the problem of transfer learning for
GMMs, where similar theoretical results are derived. Finally, we
demonstrate the effectiveness of our methods through simulations and a
real data analysis. To the best of our knowledge, this is the first work
studying multi-task and transfer learning on GMMs with theoretical
guarantees. This package implements the algorithms proposed in Tian, Y.,
Weng, H., & Feng, Y. (2022) <arXiv:2209.15224>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
