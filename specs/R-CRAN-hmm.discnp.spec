%global __brp_check_rpaths %{nil}
%global packname  hmm.discnp
%global packver   3.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.6
Release:          2%{?dist}%{?buildtag}
Summary:          Hidden Markov Models with Discrete Non-Parametric ObservationDistributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-nnet >= 7.3.12
Requires:         R-nnet >= 7.3.12

%description
Fits hidden Markov models with discrete non-parametric observation
distributions to data sets.  The observations may be univariate or
bivariate. Simulates data from such models. Finds most probable underlying
hidden states, the most probable sequences of such states, and the log
likelihood of a collection of observations given the parameters of the
model.  Auxiliary predictors are accommodated in the univariate setting.

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
