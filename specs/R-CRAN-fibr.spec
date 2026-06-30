%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fibr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Prior-Fraction Diagnostics for Hierarchical Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-posterior >= 1.4.0
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-posterior >= 1.4.0
Requires:         R-CRAN-ggplot2 

%description
Computes the prior fraction, the per-group pooling or shrinkage factor,
for hierarchical models, including directly from 'brms' fits. For each
group-level coefficient the prior fraction is the share of the posterior
precision contributed by the shrinkage prior relative to the likelihood;
values near one indicate a coefficient that is prior-dominated (the
centring/non-centring funnel regime), values near zero indicate a
likelihood-dominated coefficient that is well identified from the data.
These quantities are invisible to standard convergence diagnostics such as
R-hat and effective sample size, and they indicate where a non-centred
reparameterisation is likely to help. A companion advisor reports the same
decomposition for changepoint random effects fitted with 'smoothbp'. The
underlying geometry (the Fisher-metric connection on the base-fiber split,
for which this connection is flat so the obstruction is statistical rather
than geometric) is described in Bindoff (2026)
<doi:10.5281/zenodo.20724550>; code reproducing the paper is in the
package's source repository.

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
