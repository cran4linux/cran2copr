%global packname  tfprobability
%global packver   0.11.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'TensorFlow Probability'

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 2.2.0
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tensorflow >= 2.2.0
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
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
