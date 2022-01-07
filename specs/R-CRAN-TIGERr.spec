%global __brp_check_rpaths %{nil}
%global packname  TIGERr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Technical Variation Elimination with Ensemble Learning Architecture

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-parallel >= 2.1.0
BuildRequires:    R-CRAN-pbapply >= 1.4.3
BuildRequires:    R-CRAN-ppcor >= 1.1
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-stats >= 3.0.0
Requires:         R-parallel >= 2.1.0
Requires:         R-CRAN-pbapply >= 1.4.3
Requires:         R-CRAN-ppcor >= 1.1

%description
The R implementation of TIGER. TIGER integrates random forest algorithm
into an innovative ensemble learning architecture. Benefiting from this
advanced architecture, TIGER is resilient to outliers, free from model
tuning and less likely to be affected by specific hyperparameters. TIGER
supports targeted and untargeted metabolomics data and is competent to
perform both intra- and inter-batch technical variation removal. TIGER can
also be used for cross-kit adjustment to ensure data obtained from
different analytical assays can be effectively combined and compared.
Reference: Han S. et al. (2022) <doi:10.1093/bib/bbab535>.

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
