%global packname  rcane
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Different Numeric Optimizations to Estimate ParameterCoefficients

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
There are different numeric optimizations which are used in order to
estimate coefficients in models such as linear regression and neural
networks. This package covers parameter estimation in linear regression
using different methods such as batch gradient descent, stochastic
gradient descent, minibatch gradient descent and coordinate descent.
Kiwiel, Krzysztof C (2001) <doi:10.1007/PL00011414> Yu Nesterov (2004)
<ISBN:1-4020-7553-7> Ferguson, Thomas S (1982)
<doi:10.1080/01621459.1982.10477894> Zeiler, Matthew D (2012)
<arXiv:1212.5701> Wright, Stephen J (2015) <arXiv:1502.04759>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
