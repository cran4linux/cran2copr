%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diathor
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Ecological Information and Diatom Based Indices

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
Calculate multiple biotic indices using diatoms from environmental
samples. Diatom species are identified by their species names through a
heuristic search, and ecological data is retrieved from multiple sources.
The package includes the calculation of chloroplast diversity indices,
size classes, ecological guilds, and various biotic indices. It outputs
both a dataframe with all the results and plots of the obtained data in a
specified output folder. Sample data is sourced from Nicolosi Gelis,
Cochero, & Gómez (2020, <doi:10.1016/j.ecolind.2019.105951>). The package
utilizes the 'Diat.Barcode' database for morphological and ecological
information by Rimet & Couchez (2012, <doi:10.1051/kmae/2012018>), along
with the combined classification of guilds and size classes from B-Beres
et al. (2017, <doi:10.1016/j.ecolind.2017.07.007>). Currently supported
diatom-based biotic indices include DES index (Descy, 1979); EPID index
(Dell'Uomo, 1996); IDAP index (Prygiel & Coste, 1993); ID-CH index
(Hürlimann & Niederhauser, 2007); IDP index (Gómez & Licursi, 2001); ILM
index (Leclercq & Maquet, 1987); IPS index (Coste, 1982); LOBO index
(Lobo, Callegaro, & Bender, 2002); SLA index (Sladecek, 1986); TDI index
(Kelly & Whitton, 1995); SPEAR(herbicide) index (Wood et al., 2019); PBIDW
index (Castro-Roa & Pinilla-Agudelo, 2014); DISP index (Stenger-Kovácsa et
al., 2018).

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
