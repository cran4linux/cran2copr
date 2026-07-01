%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GSbench
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Benchmarking Genomic Selection and Machine-Learning Prediction Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
A unified interface to fit, cross-validate and benchmark genomic
prediction models from SNP marker data. It implements genomic best linear
unbiased prediction (GBLUP) and ridge-regression BLUP in base R, and
offers a common interface to machine-learning predictors (elastic net,
random forest and gradient boosting) through optional packages, together
with a stacked ensemble. Cross-validation uses breeding-relevant schemes
and reports prediction accuracy honestly, so models can be compared
fairly. The genomic relationship matrix follows VanRaden (2008)
<doi:10.3168/jds.2007-0980>; the mixed-model solver follows Endelman
(2011) <doi:10.3835/plantgenome2011.08.0024>; the genomic-selection
framework follows Meuwissen, Hayes and Goddard (2001)
<doi:10.1093/genetics/157.4.1819>.

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
