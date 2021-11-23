%global __brp_check_rpaths %{nil}
%global packname  PEkit
%global packver   1.0.0.1000
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1000
Release:          1%{?dist}%{?buildtag}
Summary:          Partition Exchangeability Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 4.1.0
Requires:         R-stats >= 4.1.0

%description
Bayesian supervised predictive classifiers, hypothesis testing, and
parametric estimation under Partition Exchangeability are implemented. The
two classifiers presented are the marginal classifier (that assumes test
data is i.i.d.) next to a more computationally costly but accurate
simultaneous classifier (that finds a labelling for the entire test
dataset at once based on simultanous use of all the test data to predict
each label). We also provide the Maximum Likelihood Estimation (MLE) of
the only underlying parameter of the partition exchangeability generative
model as well as hypothesis testing statistics for equality of this
parameter with a single value, alternative, or multiple samples. We
present functions to simulate the sequences from Ewens Sampling Formula as
the realisation of the Poisson-Dirichlet distribution and their respective
probabilities.

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
