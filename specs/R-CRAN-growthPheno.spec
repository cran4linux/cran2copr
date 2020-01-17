%global packname  growthPheno
%global packver   1.0-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.21
Release:          1%{?dist}
Summary:          Plotting, Smoothing and Growth Trait Extraction for LongitudinalData

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dae 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-grid 
Requires:         R-CRAN-dae 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape 
Requires:         R-grid 

%description
Assists in producing longitudinal or profile plots of measured traits.
These allow checks to be made for anomalous data and growth patterns in
the data to be explored. Smoothing of growth trends for individual plants
using smoothing splines is available for removing transient effects. There
are tools for diagnosing the adequacy of trait smoothing, either using
this package or other packages, such as those that fit nonlinear growth
models. A range of per-unit (pot, plant, plot) growth traits can be
extracted from longitudinal data, including single time-point smoothed
trait values and their growth rates, interval growth rates and other
growth statistics, such as maximum growth. The package is particularly
suited to preparing data from high-throughput phenotyping facilities, such
as imaging data from a Lemna-Tec Scananalyzer (see
<https://www.lemnatec.com/products/conveyor-scanalyzer/> for more
information). The package 'growthPheno' can also be installed from
<http://chris.brien.name/rpackages/>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/News.Rd
%{rlibdir}/%{packname}/INDEX
