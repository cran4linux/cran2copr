%global __brp_check_rpaths %{nil}
%global packname  kitagawa
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Spectral Response of Water Wells to Harmonic Strain and PressureSignals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-CRAN-psd >= 2.0.0
BuildRequires:    R-CRAN-kelvin >= 1.2.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Bessel 
Requires:         R-CRAN-psd >= 2.0.0
Requires:         R-CRAN-kelvin >= 1.2.0
Requires:         R-stats 
Requires:         R-CRAN-Bessel 

%description
Provides tools to calculate the theoretical hydrodynamic response of an
aquifer undergoing harmonic straining or pressurization, or analyze
measured responses. There are two classes of models here, designed for use
with confined aquifers: (1) for sealed wells, based on the model of
Kitagawa et al (2011, <doi:10.1029/2010JB007794>), and (2) for open wells,
based on the models of Cooper et al (1965, <doi:10.1029/JZ070i016p03915>),
Hsieh et al (1987, <doi:10.1029/WR023i010p01824>), Rojstaczer (1988,
<doi:10.1029/JB093iB11p13619>), Liu et al (1989,
<doi:10.1029/JB094iB07p09453>), and Wang et al (2018,
<doi:10.1029/2018WR022793>). Wang's solution is a special exception which
allows for leakage out of the aquifer (semi-confined); it is equivalent to
Hsieh's model when there is no leakage (the confined case). These models
treat strain (or aquifer head) as an input to the physical system, and
fluid-pressure (or water height) as the output. The applicable frequency
band of these models is characteristic of seismic waves, atmospheric
pressure fluctuations, and solid earth tides.

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

%files
%{rlibdir}/%{packname}
