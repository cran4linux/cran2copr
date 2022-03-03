%global __brp_check_rpaths %{nil}
%global packname  spacefillr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Space-Filling Random and Quasi-Random Sequences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Generates random and quasi-random space-filling sequences. Supports the
following sequences: 'Halton', 'Sobol', 'Owen'-scrambled 'Sobol',
'Owen'-scrambled 'Sobol' with errors distributed as blue noise,
progressive jittered, progressive multi-jittered ('PMJ'), 'PMJ' with blue
noise, 'PMJ02', and 'PMJ02' with blue noise. Includes a 'C++' 'API'.
Methods derived from "Constructing Sobol sequences with better
two-dimensional projections" (2012) <doi:10.1137/070709359> S. Joe and F.
Y. Kuo, "Progressive Multi-Jittered Sample Sequences" (2018)
<https://graphics.pixar.com/library/ProgressiveMultiJitteredSampling/paper.pdf>
Christensen, P., Kensler, A. and Kilpatrick, C., and "A Low-Discrepancy
Sampler that Distributes Monte Carlo Errors as a Blue Noise in Screen
Space" (2019) E. Heitz, B. Laurent, O. Victor, C. David and I.
Jean-Claude, <doi:10.1145/3306307.3328191>.

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
