%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NACHO
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          NanoString Quality Control Dashboard

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.25
BuildRequires:    R-CRAN-rmarkdown >= 1.16
BuildRequires:    R-CRAN-ggrepel >= 0.8.1
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.9
BuildRequires:    R-CRAN-ggforce >= 0.3.1
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-knitr >= 1.25
Requires:         R-CRAN-rmarkdown >= 1.16
Requires:         R-CRAN-ggrepel >= 0.8.1
Requires:         R-CRAN-shinyWidgets >= 0.4.9
Requires:         R-CRAN-ggforce >= 0.3.1
Requires:         R-utils 
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
