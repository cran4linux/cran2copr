%global __brp_check_rpaths %{nil}
%global packname  ggmix
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection in Linear Mixed Models for SNP Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 

%description
Fit penalized multivariable linear mixed models with a single random
effect to control for population structure in genetic association studies.
The goal is to simultaneously fit many genetic variants at the same time,
in order to select markers that are independently associated with the
response. Can also handle prior annotation information, for example, rare
variants, in the form of variable weights. For more information, see the
website below and the accompanying paper: Bhatnagar et al., "Simultaneous
SNP selection and adjustment for population structure in high dimensional
prediction models", 2020, <DOI:10.1371/journal.pgen.1008766>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
