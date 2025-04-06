%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  selectMeta
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Weight Functions in Meta Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim >= 2.0.6
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-DEoptim >= 2.0.6
Requires:         R-graphics 
Requires:         R-stats 

%description
Publication bias, the fact that studies identified for inclusion in a meta
analysis do not represent all studies on the topic of interest, is
commonly recognized as a threat to the validity of the results of a meta
analysis. One way to explicitly model publication bias is via selection
models or weighted probability distributions. In this package we provide
implementations of several parametric and nonparametric weight functions.
The novelty in Rufibach (2011) is the proposal of a non-increasing variant
of the nonparametric weight function of Dear & Begg (1992). The new
approach potentially offers more insight in the selection process than
other methods, but is more flexible than parametric approaches. To
maximize the log-likelihood function proposed by Dear & Begg (1992) under
a monotonicity constraint we use a differential evolution algorithm
proposed by Ardia et al (2010a, b) and implemented in Mullen et al (2009).
In addition, we offer a method to compute a confidence interval for the
overall effect size theta, adjusted for selection bias as well as a
function that computes the simulation-based p-value to assess the null
hypothesis of no selection as described in Rufibach (2011, Section 6).

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
