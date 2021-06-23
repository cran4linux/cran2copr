%global __brp_check_rpaths %{nil}
%global packname  FILEST
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fine-Level Structure Simulator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-KRIS >= 1.1.1
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-KRIS >= 1.1.1
Requires:         R-CRAN-rARPACK 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
A population genetic simulator, which is able to generate synthetic
datasets for single-nucleotide polymorphisms (SNP) for multiple
populations. The genetic distances among populations can be set according
to the Fixation Index (Fst) as explained in Balding and Nichols (1995)
<doi:10.1007/BF01441146>. This tool is able to simulate outlying
individuals and missing SNPs can be specified. For Genome-wide association
study (GWAS), disease status can be set in desired level according risk
ratio.

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
