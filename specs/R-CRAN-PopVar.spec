%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PopVar
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Genomic Breeding Tools: Genetic Variance Prediction and Cross-Validation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BGLR 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-rrBLUP 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-BGLR 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-rrBLUP 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-parallel 

%description
The main attribute of 'PopVar' is the prediction of genetic variance in
bi-parental populations, from which the package derives its name. 'PopVar'
contains a set of functions that use phenotypic and genotypic data from a
set of candidate parents to 1) predict the mean, genetic variance, and
superior progeny value of all, or a defined set of pairwise bi-parental
crosses, and 2) perform cross-validation to estimate genome-wide
prediction accuracy of multiple statistical models. More details are
available in Mohammadi, Tiede, and Smith (2015,
<doi:10.2135/cropsci2015.01.0030>). A dataset 'think_barley.rda' is
included for reference and examples.

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
