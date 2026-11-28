%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arcstat
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Arc-Length Statistics, Equivalence Families and Induction Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Inference from the arc length of statistical functions, and the curves of
the induction-period standards. A goodness-of-fit test based on the arc
length of the probability plot with an analytic saddlepoint null;
distributions built from the arc length of their defining curve, estimated
by L-moments; the characteristic-function arc length; a Bayesian
nonparametric arc-length test; the equivalence families of the
four-parameter kappa distribution of Hosking (1994)
<doi:10.1147/rd.383.0251> and of the beta-companion family, on which the
two standard induction-period readings coincide; and batched fits,
bootstraps and permutation tests of induction curves. One pure-C back-end,
parallel by 'OpenMP', serves this package and the 'Python' package
'arcstat'.

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
