%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rPowerSampleSize
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size Computations Controlling the Type-II Generalized Family-Wise Error Rate

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ssanv 
BuildRequires:    R-parallel 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-ssanv 
Requires:         R-parallel 

%description
The significance of mean difference tests in clinical trials is
established if at least r null hypotheses are rejected among m that are
simultaneously tested. This package enables one to compute necessary
sample sizes for single-step (Bonferroni) and step-wise procedures (Holm
and Hochberg). These three procedures control the q-generalized
family-wise error rate (probability of making at least q false
rejections). Sample size is computed (for these single-step and step-wise
procedures) in a such a way that the r-power (probability of rejecting at
least r false null hypotheses, i.e. at least r significant endpoints among
m) is above some given threshold, in the context of tests of difference of
means for two groups of continuous endpoints (variables). Various types of
structure of correlation are considered. It is also possible to analyse
data (i.e., actually test difference in means) when these are available.
The case r equals 1 is treated in separate functions that were used in
Lafaye de Micheaux et al. (2014) <doi:10.1080/10543406.2013.860156>.

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
