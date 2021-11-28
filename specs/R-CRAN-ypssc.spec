%global __brp_check_rpaths %{nil}
%global packname  ypssc
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Yeast-Proteome Secondary-Structure Calculator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spelling 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-eulerr 
BuildRequires:    R-CRAN-Peptides 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-svDialogs 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-spelling 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-eulerr 
Requires:         R-CRAN-Peptides 
Requires:         R-utils 
Requires:         R-CRAN-svDialogs 
Requires:         R-tcltk 

%description
An extension for 'NetSurfP-2.0' (Klausen et al. (2019)
<doi:10.1002/prot.25674>) which is specifically designed to analyze the
results of bottom-up-proteomics that is primarily analyzed with 'MaxQuant'
(Cox, J., Mann, M. (2008) <doi:10.1038/nbt.1511>). This tool is designed
to process a large number of yeast peptides that produced as a results of
whole yeast cell-proteome digestion and provide a coherent picture of
secondary structure of proteins.

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
