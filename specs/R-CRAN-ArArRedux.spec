%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ArArRedux
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rigorous Data Reduction and Error Propagation of Ar40 / Ar39 Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Processes noble gas mass spectrometer data to determine the isotopic
composition of argon (comprised of Ar36, Ar37, Ar38, Ar39 and Ar40)
released from neutron-irradiated potassium-bearing minerals. Then uses
these compositions to calculate precise and accurate geochronological ages
for multiple samples as well as the covariances between them. Error
propagation is done in matrix form, which jointly treats all samples and
all isotopes simultaneously at every step of the data reduction process.
Includes methods for regression of the time-resolved mass spectrometer
signals to t=0 ('time zero') for both single- and multi-collector
instruments, blank correction, mass fractionation correction, detector
intercalibration, decay corrections, interference corrections,
interpolation of the irradiation parameter between neutron fluence
monitors, and (weighted mean) age calculation. All operations are
performed on the logs of the ratios between the different argon isotopes
so as to properly treat them as 'compositional data', sensu Aitchison
[1986, The Statistics of Compositional Data, Chapman and Hall].

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
