%global packname  SunsVoc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Constructing Suns-Voc from Outdoor Time-Series I-V Curves

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ddiv 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ddiv 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlang 

%description
Suns-Voc (or Isc-Voc) curves can provide the current-voltage (I-V)
characteristics of the diode of photovoltaic cells without the effect of
series resistance. Here, Suns-Voc curves can be constructed with outdoor
time-series I-V curves [1,2,3] of full-size photovoltaic (PV) modules
instead of having to be measured in the lab. Time series of four different
power loss modes can be calculated based on obtained Suns-Voc curves. This
material is based upon work supported by the U.S. Department of Energy's
Office of Energy Efficiency and Renewable Energy (EERE) under Solar Energy
Technologies Office (SETO) Agreement Number DE-EE0008172. Jennifer L.
Braid is supported by the U.S. Department of Energy (DOE) Office of Energy
Efficiency and Renewable Energy administered by the Oak Ridge Institute
for Science and Education (ORISE) for the DOE. ORISE is managed by Oak
Ridge Associated Universities (ORAU) under DOE contract number
DE-SC0014664. [1] Wang, M. et al, 2018. <doi:10.1109/PVSC.2018.8547772>.
[2] Walters et al, 2018 <doi:10.1109/PVSC.2018.8548187>. [3] Guo, S. et
al, 2016. <doi:10.1117/12.2236939>.

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
