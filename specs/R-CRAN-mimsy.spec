%global __brp_check_rpaths %{nil}
%global packname  mimsy
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate MIMS Dissolved Gas Concentrations Without Getting aHeadache

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-openxlsx 
Requires:         R-utils 

%description
Calculate dissolved gas concentrations from raw MIMS (Membrane Inlet Mass
Spectrometer) signal data. Use mimsy() on a formatted CSV file to return
dissolved gas concentrations (mg and microMole) of N2, O2, Ar based on gas
solubility at temperature, pressure, and salinity. See references Benson
and Krause (1984) <DOI:10.4319/lo.1992.37.6.1307>, Garcia and Gordon
(1992) <DOI:10.4319/lo.1984.29.3.0620>, Stull (1947)
<DOI:10.1021/ie50448a022>, and Hamme and Emerson (2004)
<DOI:10.1016/j.dsr.2004.06.009> for more information. Easily save the
output to a nicely-formatted multi-tab 'Excel' workbook with mimsy.save().
Supports dual-temperature standard calibration for dual-bath MIMS setups.

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
