%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stats4teaching
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Pedagogical Statistical Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-asbio 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MVN 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-stats 
Requires:         R-CRAN-asbio 
Requires:         R-CRAN-car 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MVN 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-rstatix 
Requires:         R-stats 

%description
Univariate and multivariate normal data simulation. They also supply a
brief summary of the analysis for each experiment/design: - Independent
samples. - One-way and two-way Anova. - Paired samples (T-Test &
Regression). - Repeated measures (Anova & Multiple Regression). - Clinical
Assay.

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
