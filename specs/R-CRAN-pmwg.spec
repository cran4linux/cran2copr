%global packname  pmwg
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Particle Metropolis Within Gibbs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-condMVNorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-condMVNorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Provides an R implementation of the Particle Metropolis within Gibbs
sampler for model parameter, covariance matrix and random effect
estimation. A more general implementation of the sampler based on the
paper by Gunawan, D., Hawkins, G. E., Tran, M. N., Kohn, R., & Brown, S.
D. (2020) <doi:10.1016/j.jmp.2020.102368>. An HTML tutorial document
describing the package is available at
<https://newcastlecl.github.io/samplerDoc/> and includes several detailed
examples, some background and troubleshooting steps.

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
