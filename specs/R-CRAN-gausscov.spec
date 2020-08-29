%global packname  gausscov
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          The Gaussian Covariate Method for Variable Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Given the standard linear model the traditional way of deciding whether to
include the jth covariate is to apply the F-test to decide whether the
corresponding beta coefficient is zero. The Gaussian covariate method is
completely different. The question as to whether the beta coefficient is
or is not zero is replaced by the question as to whether the covariate is
better or worse than i.i.d. Gaussian noise. The P-value for the covariate
is the probability that Gaussian noise is better. Surprisingly this can be
given exactly and it is the same a the P-value for the classical model
based on the F-distribution. The Gaussian covariate P-value is model free,
it is the same for any data set. Using the idea it is possible to do
covariate selection for a small number of covariates 25 by considering all
subsets.  Post selection inference causes no problems as the P-values hold
whatever the data. The idea extends to stepwise regression again with
exact probabilities. In the simplest version the only parameter is a
specified cut-off P-value which can be interpreted as the probability of a
false positive being included in the final selection. For more information
see the website below and the accompanying papers: L. Davies and L.
Duembgen, "Covariate Selection Based on a Model-free Approach to Linear
Regression with Exact Probabilities", 2020, <arXiv:1906.01990>. L. Davies,
"Lasso, Knockoff and Gaussian covariates: A comparison", 2018,
<arXiv:1807.09633>.

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
