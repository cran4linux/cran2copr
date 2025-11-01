%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hirisplexr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          From 'PLINK' to 'HIrisPlex'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-BEDMatrix 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
Requires:         R-CRAN-BEDMatrix 
Requires:         R-CRAN-data.table 
Requires:         R-utils 

%description
Read 'PLINK' 1.9 binary datasets (BED/BIM/FAM) and generate the CSV files
required by the Erasmus MC 'HIrisPlex' / 'HIrisPlex-S' webtool
<https://hirisplex.erasmusmc.nl/>. It maps 'PLINK' alleles to the
webtool's required 'rsID_Allele' columns (0/1/2/NA). No external tools
(e.g., 'PLINK CLI') are required.

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
