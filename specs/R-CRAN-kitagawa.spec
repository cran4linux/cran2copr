%global packname  kitagawa
%global packver   2.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          2%{?dist}
Summary:          Spectral Response of Water Wells to Harmonic Strain and PressureSignals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-CRAN-kelvin >= 1.2.0
BuildRequires:    R-stats 
Requires:         R-CRAN-kelvin >= 1.2.0
Requires:         R-stats 

%description
Provides tools to calculate the theoretical hydrodynamic response of an
aquifer undergoing harmonic straining or pressurization, or analyze
measured responses. There are two classes of models here: (1) for sealed
wells, based on the model of Kitagawa et al (2011,
<doi:10.1029/2010JB007794>), and (2) for open wells, based on the models
of Cooper et al (1965, <doi:10.1029/JZ070i016p03915>), Hsieh et al (1987,
<doi:10.1029/WR023i010p01824>), Rojstaczer (1988,
<doi:10.1029/JB093iB11p13619>), and Liu et al (1989,
<doi:10.1029/JB094iB07p09453>). These models treat strain (or aquifer
head) as an input to the physical system, and fluid-pressure (or water
height) as the output. The applicable frequency band of these models is
characteristic of seismic waves, atmospheric pressure fluctuations, and
solid earth tides.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
