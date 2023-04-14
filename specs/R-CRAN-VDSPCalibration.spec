%global __brp_check_rpaths %{nil}
%global packname  VDSPCalibration
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Methods for Designing and Analyzing a CalibrationStudy

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides statistical methods for the design and analysis of a calibration
study, which aims for calibrating measurements using two different
methods. The package includes sample size calculation, sample selection,
regression analysis with error-in measurements and change-point
regression. The method is described in Tian, Durazo-Arvizu, Myers, et al.
(2014) <DOI:10.1002/sim.6235>.

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
