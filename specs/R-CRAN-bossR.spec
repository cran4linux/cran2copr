%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bossR
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Biomarker Optimal Segmentation System

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-survival 
Requires:         R-stats 

%description
The Biomarker Optimal Segmentation System R package, 'bossR', is designed
for precision medicine, helping to identify individual traits using
biomarkers. It focuses on determining the most effective cutoff value for
a continuous biomarker, which is crucial for categorizing patients into
two groups with distinctly different clinical outcomes. The package
simultaneously finds the optimal cutoff from given candidate values and
tests its significance. Simulation studies demonstrate that 'bossR' offers
statistical power and false positive control non-inferior to the
permutation approach (considered the gold standard in this field), while
being hundreds of times faster.

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
