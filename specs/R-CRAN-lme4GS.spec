%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lme4GS
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'lme4' for Genomic Selection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.3
Requires:         R-core >= 3.6.3
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
Flexible functions that use 'lme4' as computational engine for fitting
models used in Genomic Selection (GS). GS is a technology used for genetic
improvement, and it has many advantages over phenotype-based selection.
There are several statistical models that adequately approach the
statistical challenges in GS, such as in linear mixed models (LMMs). The
'lme4' is the standard package for fitting linear and generalized LMMs in
the R-package, but its use for genetic analysis is limited because it does
not allow the correlation between individuals or groups of individuals to
be defined. The 'lme4GS' package is focused on fitting LMMs with
covariance structures defined by the user, bandwidth selection, and
genomic prediction. The new package is focused on genomic prediction of
the models used in GS and can fit LMMs using different variance-covariance
matrices. Several examples of GS models are presented using this package
as well as the analysis using real data. For more details see Caamal-Pat
et.al. (2021) <doi:10.3389/fgene.2021.680569>.

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
