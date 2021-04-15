%global packname  ddiv
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Driven I-v Feature Extraction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qpdf >= 1.1
BuildRequires:    R-CRAN-MASS >= 0.5.3.0
BuildRequires:    R-CRAN-segmented >= 0.5.3.0
Requires:         R-CRAN-qpdf >= 1.1
Requires:         R-CRAN-MASS >= 0.5.3.0
Requires:         R-CRAN-segmented >= 0.5.3.0

%description
The Data Driven I-V Feature Extraction is used to extract Current-Voltage
(I-V) features from I-V curves. I-V curves indicate the relationship
between current and voltage for a solar cell or Photovoltaic (PV) modules.
The I-V features such as maximum power point (Pmp), shunt resistance
(Rsh), series resistance (Rs),short circuit current (Isc), open circuit
voltage (Voc), fill factor (FF), current at maximum power (Imp) and
voltage at maximum power(Vmp) contain important information of the
performance for PV modules. The traditional method uses the single diode
model to model I-V curves and extract I-V features. This package does not
use the diode model, but uses data-driven a method which select different
linear parts of the I-V curves to extract I-V features. This method also
uses a sampling method to calculate uncertainties when extracting I-V
features. Also, because of the partially shaded array, "steps" occurs in
I-V curves. The "Segmented Regression" method is used to identify steps in
I-V curves. This material is based upon work supported by the U.S.
Department of Energy’s Office of Energy Efficiency and Renewable Energy
(EERE) under Solar Energy Technologies Office (SETO) Agreement Number
DE-EE0007140. Further information can be found in the following paper. [1]
Ma, X. et al, 2019. <doi:10.1109/JPHOTOV.2019.2928477>.

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
