%global __brp_check_rpaths %{nil}
%global packname  parallelMCMCcombine
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Combining Subset MCMC Samples to Estimate a Posterior Density

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
See Miroshnikov and Conlon (2014) <doi:10.1371/journal.pone.0108425>.
Recent Bayesian Markov chain Monto Carlo (MCMC) methods have been
developed for big data sets that are too large to be analyzed using
traditional statistical methods. These methods partition the data into
non-overlapping subsets, and perform parallel independent Bayesian MCMC
analyses on the data subsets, creating independent subposterior samples
for each data subset. These independent subposterior samples are combined
through four functions in this package, including averaging across subset
samples, weighted averaging across subsets samples, and kernel smoothing
across subset samples. The four functions assume the user has previously
run the Bayesian analysis and has produced the independent subposterior
samples outside of the package; the functions use as input the array of
subposterior samples. The methods have been demonstrated to be useful for
Bayesian MCMC models including Bayesian logistic regression, Bayesian
Gaussian mixture models and Bayesian hierarchical Poisson-Gamma models.
The methods are appropriate for Bayesian hierarchical models with
hyperparameters, as long as data values in a single level of the hierarchy
are not split into subsets.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
