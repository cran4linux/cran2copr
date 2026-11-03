%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NACHO
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          NanoString Quality Control Dashboard

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-yaml >= 2.3.12
BuildRequires:    R-CRAN-scales >= 1.4.0
BuildRequires:    R-CRAN-promises >= 1.3.2
BuildRequires:    R-CRAN-shiny >= 1.11.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-ggrepel >= 0.9.6
BuildRequires:    R-CRAN-htmltools >= 0.5.9
BuildRequires:    R-CRAN-ggforce >= 0.5.0
BuildRequires:    R-CRAN-S7 >= 0.2.2
BuildRequires:    R-CRAN-bslib >= 0.10.0
BuildRequires:    R-CRAN-brand.yml >= 0.1.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-yaml >= 2.3.12
Requires:         R-CRAN-scales >= 1.4.0
Requires:         R-CRAN-promises >= 1.3.2
Requires:         R-CRAN-shiny >= 1.11.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-ggrepel >= 0.9.6
Requires:         R-CRAN-htmltools >= 0.5.9
Requires:         R-CRAN-ggforce >= 0.5.0
Requires:         R-CRAN-S7 >= 0.2.2
Requires:         R-CRAN-bslib >= 0.10.0
Requires:         R-CRAN-brand.yml >= 0.1.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-data.table 

%description
NanoString nCounter data are gene expression assays where there is no need
for the use of enzymes or amplification protocols and work with
fluorescent barcodes (Geiss et al. (2018) <doi:10.1038/nbt1385>). Each
barcode is assigned a messenger-RNA/micro-RNA (mRNA/miRNA) which after
bonding with its target can be counted. As a result each count of a
specific barcode represents the presence of its target mRNA/miRNA. 'NACHO'
(NAnoString quality Control dasHbOard) is able to analyse the exported
NanoString nCounter data and facilitates the user in performing a quality
control. 'NACHO' does this by visualising quality control metrics,
expression of control genes, principal components and sample specific size
factors in an interactive web application.

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
