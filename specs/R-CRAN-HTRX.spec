%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HTRX
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Haplotype Trend Regression with eXtra Flexibility (HTRX)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fastglm 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-recipes 
Requires:         R-CRAN-fastglm 
Requires:         R-CRAN-caret 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-recipes 

%description
Detection of haplotype patterns that include single nucleotide
polymorphisms (SNPs) and non-contiguous haplotypes that are associated
with a phenotype. Methods for implementing HTRX are described in Yang Y,
Lawson DJ (2022) <doi:10.1101/2022.11.29.518395> and Barrie W, Yang Y,
Attfield K E, et al (2022) <doi:10.1101/2022.09.23.509097>.

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
