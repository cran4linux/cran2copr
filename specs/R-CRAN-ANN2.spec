%global packname  ANN2
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Artificial Neural Networks for Anomaly Detection

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-viridisLite >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-viridisLite >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-methods 

%description
Training of neural networks for classification and regression tasks using
mini-batch gradient descent. Special features include a function for
training autoencoders, which can be used to detect anomalies, and some
related plotting functions. Multiple activation functions are supported,
including tanh, relu, step and ramp. For the use of the step and ramp
activation functions in detecting anomalies using autoencoders, see
Hawkins et al. (2002) <doi:10.1007/3-540-46145-0_17>. Furthermore, several
loss functions are supported, including robust ones such as Huber and
pseudo-Huber loss, as well as L1 and L2 regularization. The possible
options for optimization algorithms are RMSprop, Adam and SGD with
momentum. The package contains a vectorized C++ implementation that
facilitates fast training through mini-batch learning.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cereal
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
