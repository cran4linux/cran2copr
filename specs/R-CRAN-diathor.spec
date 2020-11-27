%global packname  diathor
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
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
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 

%description
Calculates ecological information and biotic indices for diatoms in a
sample. It includes number/shape of chloroplasts diversity indices, size
classes, ecological guilds, and multiple biotic indices. It outputs both a
dataframe with all the results and plots of all the obtained data in a
defined output folder. Sample data was taken from Nicolosi Gelis, Cochero
& Gómez (2020, <doi:10.1016/j.ecolind.2019.105951>). The package uses the
'Diat.Barcode' database to calculate morphological and ecological
information by Rimet & Couchez (2012, <doi:10.1051/kmae/2012018>), and
calculates the DES index by Descy (1979,
<http://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=PASCAL8060205402>),
the EPID index by Dell'Uomo (1996, ISBN: 3950009002), the IDAP index by
Prygiel & Coste (1993, <doi:10.1007/BF00028033>), the ID-CH index by
Hürlimann & Niederhauser (2007,
<https://www.bafu.admin.ch/bafu/fr/home/themes/eaux/publications/publications-eaux/methodes-analyse-appreciation-cours-eau-diatomees.html>),
the IDP index by Gómez & Licursi (2001, <doi:10.1023/A:1011415209445>),
the ILM index by Leclercq & Maquet (1987,
<http://www.vliz.be/imisdocs/publications/286641.pdf>), the IPS index by
Coste (1982,
<https://www.oieau.org/eaudoc/notice/ETUDE-DES-METHODES-BIOLOGIQUES-DAPPRECIATION-QUANTITATIVE-DE-LA-QUALITE-DES-EAUX>),
the LOBO index by Lobo, Callegaro, & Bender (2002, ISBN:9788585869908),
the SLA by Sládeček (1986, <doi:10.1002/aheh.19860140519>), the TDI index
by Kelly, & Whitton (1995, <doi:10.1007/BF00003802>), and the
SPEAR(herbicide) index by Wood, Mitrovic, Lim, Warne, Dunlop, & Kefford
(2019, <doi:10.1016/j.ecolind.2018.12.035>).

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
