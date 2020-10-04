%global packname  RegressionFactory
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          3%{?dist}%{?buildtag}
Summary:          Expander Functions for Generating Full Gradient and Hessian fromSingle-Slot and Multi-Slot Base Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The expander functions rely on the mathematics developed for the
Hessian-definiteness invariance theorem for linear projection
transformations of variables, described in authors' paper, to generate the
full, high-dimensional gradient and Hessian from the lower-dimensional
derivative objects. This greatly relieves the computational burden of
generating the regression-function derivatives, which in turn can be fed
into any optimization routine that utilizes such derivatives. The theorem
guarantees that Hessian definiteness is preserved, meaning that reasoning
about this property can be performed in the low-dimensional space of the
base distribution. This is often a much easier task than its equivalent in
the full, high-dimensional space. Definiteness of Hessian can be useful in
selecting optimization/sampling algorithms such as Newton-Raphson
optimization or its sampling equivalent, the Stochastic Newton Sampler.
Finally, in addition to being a computational tool, the regression
expansion framework is of conceptual value by offering new opportunities
to generate novel regression problems.

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
