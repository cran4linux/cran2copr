%global __brp_check_rpaths %{nil}
%global packname  GrimR
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Calculate Optical Parameters from Spindle Stage Measurements

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-stats4 
Requires:         R-CRAN-car 
Requires:         R-stats4 

%description
Calculates optical parameters of crystals like the optical axes, the axis
angle 2V, and the direction of the principal axes of the indicatrix from
extinction angles measured on a spindle stage mounted on a polarisation
microscope stage. Details of the method can be found in Dufey (2017)
<arXiv:1703.00070>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
