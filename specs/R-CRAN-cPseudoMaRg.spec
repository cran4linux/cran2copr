%global __brp_check_rpaths %{nil}
%global packname  cPseudoMaRg
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Constructs a Correlated Pseudo-Marginal Sampler

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The primary function makeCPMSampler() generates a sampler function which
performs the correlated pseudo-marginal method of Deligiannidis, Doucet
and Pitt (2017) <arXiv:1511.04992>. If the 'rho=' argument of
makeCPMSampler() is set to 0, then the generated sampler function performs
the original pseudo-marginal method of Andrieu and Roberts (2009)
<DOI:10.1214/07-AOS574>. The sampler function is constructed with the
user's choice of prior, parameter proposal distribution, and the
likelihood approximation scheme. Note that this algorithm is not
automatically tuned--each one of these arguments must be carefully chosen.

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
