%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  compound.Cox
%global packver   3.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.29
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate Feature Selection and Compound Covariate for Predicting Survival

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 

%description
Univariate feature selection and compound covariate methods under the Cox
model with high-dimensional features (e.g., gene expressions). Available
are survival data for non-small-cell lung cancer patients with gene
expressions (Chen et al 2007 New Engl J Med) <DOI:10.1056/NEJMoa060096>,
statistical methods in Emura et al (2012 PLoS ONE)
<DOI:10.1371/journal.pone.0047627>, Emura & Chen (2016 Stat Methods Med
Res) <DOI:10.1177/0962280214533378>, and Emura et al
(2019)<DOI:10.1016/j.cmpb.2018.10.020>. Algorithms for generating
correlated gene expressions are also available. Estimation of survival
functions via copula-graphic (CG) estimators is also implemented, which is
useful for sensitivity analyses under dependent censoring (Yeh et al 2023)
<DOI:10.3390/biomedicines11030797>.

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
