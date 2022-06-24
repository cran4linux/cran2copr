%global __brp_check_rpaths %{nil}
%global packname  MOST
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multiphase Optimization Strategy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch

%description
Provides functions similar to the 'SAS' macros previously provided to
accompany Collins, Dziak, and Li (2009) <DOI:10.1037/a0015826> and Dziak,
Nahum-Shani, and Collins (2012) <DOI:10.1037/a0026972>, papers which
outline practical benefits and challenges of factorial and fractional
factorial experiments for scientists interested in developing biological
and/or behavioral interventions, especially in the context of the
multiphase optimization strategy (see Collins, Kugler & Gwadz 2016)
<DOI:10.1007/s10461-015-1145-4>.  The package currently contains three
functions. First, RelativeCosts1() draws a graph of the relative cost of
complete and reduced factorial designs versus other alternatives. Second,
RandomAssignmentGenerator() returns a dataframe which contains a list of
random numbers that can be used to conveniently assign participants to
conditions in an experiment with many conditions. Third,
FactorialPowerPlan() estimates the power, detectable effect size, or
required sample size of a factorial or fractional factorial experiment,
for main effects or interactions, given several possible choices of effect
size metric, and allowing pretests and clustering.

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
