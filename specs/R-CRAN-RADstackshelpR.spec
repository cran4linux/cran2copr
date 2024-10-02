%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RADstackshelpR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimize the De Novo Stacks Pipeline via R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vcfR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-vcfR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-gridExtra 

%description
Offers a handful of useful wrapper functions which streamline the reading,
analyzing, and visualizing of variant call format (vcf) files in R. This
package was designed to facilitate an explicit pipeline for optimizing
Stacks (Rochette et al., 2019) (<doi:10.1111/mec.15253>) parameters during
de novo (without a reference genome) assembly and variant calling of
restriction-enzyme associated DNA sequence (RADseq) data. The pipeline
implemented here is based on the 2017 paper "Lost in Parameter Space"
(Paris et al., 2017) (<doi:10.1111/2041-210X.12775>) which establishes
clear recommendations for optimizing the parameters 'm', 'M', and 'n',
during the process of assembling loci.

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
