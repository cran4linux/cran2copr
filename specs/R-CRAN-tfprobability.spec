%global packname  tfprobability
%global packver   0.10.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0.0
Release:          2%{?dist}
Summary:          Interface to 'TensorFlow Probability'

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 2.1.0
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tensorflow >= 2.1.0
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-magrittr 

%description
Interface to 'TensorFlow Probability', a 'Python' library built on
'TensorFlow' that makes it easy to combine probabilistic models and deep
learning on modern hardware ('TPU', 'GPU'). 'TensorFlow Probability'
includes a wide selection of probability distributions and bijectors,
probabilistic layers, variational inference, Markov chain Monte Carlo, and
optimizers such as Nelder-Mead, BFGS, and SGLD.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
