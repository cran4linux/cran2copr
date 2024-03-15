%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StructFDR
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          False Discovery Control Procedure Integrating the Prior Structure Information

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dirmult 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dirmult 
Requires:         R-CRAN-matrixStats 

%description
Perform more powerful false discovery control (FDR) for microbiome data,
taking into account the prior phylogenetic relationship among bacteria
species.  As a general methodology, it is applicable to any type of
(genomic) data with prior structure information.

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
