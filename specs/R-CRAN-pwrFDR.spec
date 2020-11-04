%global packname  pwrFDR
%global packver   2.8.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.6
Release:          1%{?dist}%{?buildtag}
Summary:          FDR Power

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
This is a package for calculating two differing notions of power, or
deriving sample sizes for specified requisite power in multiple testing
experiments under a variety of methods for control of the distribution of
the False Discovery Proportion (FDP). More specifically, one can choose to
control the FDP distribution according to control of its (i) mean, e.g.
the usual BH-FDR procedure, or via the probability that it exceeds a given
value, delta, via (ii) the Romano procedure, or via (iii) my procedure
based upon asymptotic approximation. Likewise, we can think of the power
in multiple testing experiments in terms of a summary of the distribution
of the True Positive Proportion (TPP). The package will compute power,
sample size or any other missing parameter required for power based upon
(i) the mean of the TPP which is the average power (ii) the probability
that the TPP exceeds a given value, lambda, via my asymptotic
approximation procedure. The theoretical results are described in
Izmirlian, G. (2020) Stat. and Prob. letters,
<doi:10.1016/j.spl.2020.108713>, and an applied paper describing the
methodology with a simulation study is in preparation.

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
