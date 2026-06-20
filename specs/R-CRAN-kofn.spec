%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kofn
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Estimation for k-Out-of-n System Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flexhaz >= 0.5.2
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-likelihood.model 
BuildRequires:    R-CRAN-compositional.mle 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-dist.structure 
BuildRequires:    R-CRAN-algebraic.dist 
Requires:         R-CRAN-flexhaz >= 0.5.2
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-likelihood.model 
Requires:         R-CRAN-compositional.mle 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-dist.structure 
Requires:         R-CRAN-algebraic.dist 

%description
Maximum likelihood estimation of component lifetime parameters from
system-level observations of k-out-of-n systems. Supports exponential and
Weibull component distributions under multiple observation schemes: Scheme
0 (system lifetime only), Scheme 1 (periodic inspection), and Scheme 2
(complete monitoring). Provides an EM algorithm for Weibull parallel
systems and Fisher information comparison across schemes. The k-out-of-n
framework unifies series (k=1) and parallel (k=m) systems as a censoring
problem on component lifetimes. Conforms to the 'likelihood.model'
generics and returns fitted objects compatible with 'algebraic.mle'. The
data-generating process and topology infrastructure (system survival,
density, signature, structure function, importance measures) are delegated
to the 'dist.structure' package; 'kofn' focuses exclusively on inference
for the k-out-of-n family.

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
