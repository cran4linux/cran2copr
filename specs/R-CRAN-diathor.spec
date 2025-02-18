%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diathor
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
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
samples. Diatom species are recognized by their species' name using a
heuristic search, and their ecological data is retrieved from multiple
sources. It includes number/shape of chloroplasts diversity indices, size
classes, ecological guilds, and multiple biotic indices. It outputs both a
dataframe with all the results and plots of all the obtained data in a
defined output folder. - Sample data was taken from Nicolosi Gelis,
Cochero & Gómez (2020, <doi:10.1016/j.ecolind.2019.105951>). - The package
uses the 'Diat.Barcode' database to calculate morphological and ecological
information by Rimet & Couchez (2012, <doi:10.1051/kmae/2012018>),and the
combined classification of guilds and size classes established by B-Béres
et al. (2017, <doi:10.1016/j.ecolind.2017.07.007>). - Current diatom-based
biotic indices include the DES index by Descy (1979) - EPID index by
Dell'Uomo (1996, ISBN: 3950009002) - IDAP index by Prygiel & Coste (1993,
<doi:10.1007/BF00028033>) - ID-CH index by Hürlimann & Niederhauser (2007)
- IDP index by Gómez & Licursi (2001, <doi:10.1023/A:1011415209445>) - ILM
index by Leclercq & Maquet (1987) - IPS index by Coste (1982) - LOBO index
by Lobo, Callegaro, & Bender (2002, ISBN:9788585869908) - SLA by Sládeček
(1986, <doi:10.1002/aheh.19860140519>) - TDI index by Kelly, & Whitton
(1995, <doi:10.1007/BF00003802>) - SPEAR(herbicide) index by Wood,
Mitrovic, Lim, Warne, Dunlop, & Kefford (2019,
<doi:10.1016/j.ecolind.2018.12.035>) - PBIDW index by Castro-Roa &
Pinilla-Agudelo (2014) - DISP index by Stenger-Kovács et al. (2018,
<doi:10.1016/j.ecolind.2018.07.026>) - EDI index by Chamorro et al. (2024,
<doi:10.1021/acsestwater.4c00126>) - DDI index by Álvarez-Blanco et al.
(2013, <doi: 10.1007/s10661-012-2607-z>) - PDISE index by Kahlert et al.
(2023, <doi:10.1007/s10661-023-11378-4>).

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
