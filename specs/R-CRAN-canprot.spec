%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  canprot
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Chemical Analysis of Proteins

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-multcompView 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-multcompView 

%description
Chemical analysis of proteins based on their amino acid compositions.
Amino acid compositions can be read from FASTA files and used to calculate
chemical metrics including carbon oxidation state and stoichiometric
hydration state, as described in Dick et al. (2020)
<doi:10.5194/bg-17-6145-2020>. Other properties that can be calculated
include protein length, grand average of hydropathy (GRAVY), isoelectric
point (pI), molecular weight (MW), standard molal volume (V0), and
metabolic costs (Akashi and Gojobori, 2002 <doi:10.1073/pnas.062526999>;
Wagner, 2005 <doi:10.1093/molbev/msi126>; Zhang et al., 2018
<doi:10.1038/s41467-018-06461-1>). A database of amino acid compositions
of human proteins derived from UniProt is provided.

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
