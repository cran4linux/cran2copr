%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tseLCA
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Three-Step Estimation for Latent Class Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multilevLCA 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-multilevLCA 
Requires:         R-CRAN-cli 

%description
Implements BCH (Bolck-Croon-Hagenaars) <doi:10.1093/pan/mph001> and ML
(Vermunt's maximum likelihood) <doi:10.1093/pan/mpq025> approaches for
three-step estimation of latent class models with covariates and distal
outcomes, following Bakk, Tekle & Vermunt (2013)
<doi:10.1177/0081175012470644>, Bakk, Oberski & Vermunt (2014)
<https://www.jstor.org/stable/24573086>, and Bakk & Kuha (2018)
<doi:10.1007/s11336-017-9592-7>. Built on 'multilevLCA' (Lyrvall et al.,
2025) <doi:10.1080/00273171.2025.2473935> for Step-1 measurement model
estimation, this package extends it with support for Gaussian, Poisson,
and binomial distal outcome families. Unlike 'poLCA', which relies on
one-step estimation and cannot accommodate a measurement model from a
different sample, this package uses a stepwise approach to prevent the
structural model from influencing latent class formation. Implements
correct sandwich variance estimation that propagates measurement
uncertainty from the first-step through classification-error correction in
the final step (Bakk, Oberski & Vermunt, 2014). Supports polytomous items
and missing data in the measurement model with full information maximum
likelihood. A data-generating process replicating the Bakk & Kuha (2018)
simulation study is included.

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
