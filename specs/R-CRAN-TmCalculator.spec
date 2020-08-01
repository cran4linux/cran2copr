%global packname  TmCalculator
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Melting Temperature of Nucleic Acid Sequences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
This tool is extended from methods in Bio.SeqUtils.MeltingTemp of python.
The melting temperature of nucleic acid sequences can be calculated in
three method, the Wallace rule (Thein & Wallace (1986)
<doi:10.1016/S0140-6736(86)90739-7>), empirical formulas based on G and C
content (Marmur J. (1962) <doi:10.1016/S0022-2836(62)80066-7>, Schildkraut
C. (2010) <doi:10.1002/bip.360030207>, Wetmur J G (1991)
<doi:10.3109/10409239109114069>, Untergasser,A. (2012)
<doi:10.1093/nar/gks596>, von Ahsen N (2001)
<doi:10.1093/clinchem/47.11.1956>) and nearest neighbor thermodynamics
(Breslauer K J (1986) <doi:10.1073/pnas.83.11.3746>, Sugimoto N (1996)
<doi:10.1093/nar/24.22.4501>, Allawi H (1998)
<doi:10.1093/nar/26.11.2694>, SantaLucia J (2004)
<doi:10.1146/annurev.biophys.32.110601.141800>, Freier S (1986)
<doi:10.1073/pnas.83.24.9373>, Xia T (1998) <doi:10.1021/bi9809425>, Chen
JL (2012) <doi:10.1021/bi3002709>, Bommarito S (2000)
<doi:10.1093/nar/28.9.1929>, Turner D H (2010) <doi:10.1093/nar/gkp892>,
Sugimoto N (1995) <doi:10.1016/S0048-9697(98)00088-6>, Allawi H T (1997)
<doi:10.1021/bi962590c>, Santalucia N (2005) <doi:10.1093/nar/gki918>),
and it can also be corrected with salt ions and chemical compound
(SantaLucia J (1996) <doi:10.1021/bi951907q>, SantaLucia J(1998)
<doi:10.1073/pnas.95.4.1460>, Owczarzy R (2004) <doi:10.1021/bi034621r>,
Owczarzy R (2008) <doi:10.1021/bi702363u>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
