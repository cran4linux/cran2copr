%global packname  stochQN
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Limited Memory Quasi-Newton Optimizers

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Implementations of stochastic, limited-memory quasi-Newton optimizers,
similar in spirit to the LBFGS (Limited-memory
Broyden-Fletcher-Goldfarb-Shanno) algorithm, for smooth stochastic
optimization. Implements the following methods: oLBFGS (online LBFGS)
(Schraudolph, N.N., Yu, J. and Guenter, S., 2007
<http://proceedings.mlr.press/v2/schraudolph07a.html>), SQN (stochastic
quasi-Newton) (Byrd, R.H., Hansen, S.L., Nocedal, J. and Singer, Y., 2016
<arXiv:1401.7020>), adaQN (adaptive quasi-Newton) (Keskar, N.S., Berahas,
A.S., 2016, <arXiv:1511.01169>). Provides functions for easily creating R
objects with partial_fit/predict methods from some given
objective/gradient/predict functions. Includes an example stochastic
logistic regression using these optimizers. Provides header files and
registered C routines for using it directly from C/C++.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
