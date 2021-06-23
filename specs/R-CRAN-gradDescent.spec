%global __brp_check_rpaths %{nil}
%global packname  gradDescent
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Gradient Descent for Regression Tasks

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
An implementation of various learning algorithms based on Gradient Descent
for dealing with regression tasks. The variants of gradient descent
algorithm are : Mini-Batch Gradient Descent (MBGD), which is an
optimization to use training data partially to reduce the computation
load. Stochastic Gradient Descent (SGD), which is an optimization to use a
random data in learning to reduce the computation load drastically.
Stochastic Average Gradient (SAG), which is a SGD-based algorithm to
minimize stochastic step to average. Momentum Gradient Descent (MGD),
which is an optimization to speed-up gradient descent learning.
Accelerated Gradient Descent (AGD), which is an optimization to accelerate
gradient descent learning. Adagrad, which is a gradient-descent-based
algorithm that accumulate previous cost to do adaptive learning. Adadelta,
which is a gradient-descent-based algorithm that use hessian approximation
to do adaptive learning. RMSprop, which is a gradient-descent-based
algorithm that combine Adagrad and Adadelta adaptive learning ability.
Adam, which is a gradient-descent-based algorithm that mean and variance
moment to do adaptive learning. Stochastic Variance Reduce Gradient
(SVRG), which is an optimization SGD-based algorithm to accelerates the
process toward converging by reducing the gradient. Semi Stochastic
Gradient Descent (SSGD),which is a SGD-based algorithm that combine GD and
SGD to accelerates the process toward converging by choosing one of the
gradients at a time. Stochastic Recursive Gradient Algorithm (SARAH),
which is an optimization algorithm similarly SVRG to accelerates the
process toward converging by accumulated stochastic information.
Stochastic Recursive Gradient Algorithm+ (SARAHPlus), which is a SARAH
practical variant algorithm to accelerates the process toward converging
provides a possibility of earlier termination.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
