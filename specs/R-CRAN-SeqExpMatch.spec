%global __brp_check_rpaths %{nil}
%global packname  SeqExpMatch
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Experimental Design via Matching on-the-Fly

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.3
Requires:         R-core >= 3.6.3
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-doParallel 
Requires:         R-stats 

%description
Generates the following sequential two-arm experimental designs: (1)
completely randomized (Bernoulli) (2) balanced completely randomized (3)
Efron's (1971) Biased Coin (4) Atkinson's (1982) Covariate-Adjusted Biased
Coin (5) Kapelner and Krieger's (2014) Covariate-Adjusted Matching on the
Fly (6) Kapelner and Krieger's (2021) CARA Matching on the Fly with
Differential Covariate Weights (Naive) (7) Kapelner and Krieger's (2021)
CARA Matching on the Fly with Differential Covariate Weights (Stepwise)
and also provides the following types of inference: (1) estimation (with
both Z-style estimators and OLS estimators), (2) frequentist testing (via
asymptotic distribution results and via employing the nonparametric
randomization test) and (3) frequentist confidence intervals (only under
the superpopulation sampling assumption currently). Details can be found
in our publication: Kapelner and Krieger "A Matching Procedure for
Sequential Experiments that Iteratively Learns which Covariates Improve
Power" (2020) <arXiv:2010.05980>.

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
