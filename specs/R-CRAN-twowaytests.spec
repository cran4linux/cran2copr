%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  twowaytests
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Way Tests in Independent Groups Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-onewaytests 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-wesanderson 
Requires:         R-CRAN-onewaytests 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-car 
Requires:         R-CRAN-wesanderson 

%description
Performs two-way tests in independent groups designs. These are two-way
ANOVA, two-way ANOVA under heteroscedasticity: parametric bootstrap based
generalized test and generalized pivotal quantity based generalized test
(Ananda et al., 2022) <doi:10.1080/03610926.2022.2059682>, two-way ANOVA
for medians, trimmed means, M-estimators (Wilcox, 2011;
ISBN:978-0-12-386983-8). The package performs descriptive statistics and
graphical approaches. Moreover, it assesses variance homogeneity and
normality of data in each group via tests and plots. All 'twowaytests'
functions are designed for two-way layout.

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
