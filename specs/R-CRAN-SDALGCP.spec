%global packname  SDALGCP
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Spatially Discrete Approximation to Log-Gaussian Cox Processesfor Aggregated Disease Count Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-mapview >= 2.6.0
BuildRequires:    R-CRAN-splancs >= 2.1.40
BuildRequires:    R-CRAN-geoR >= 1.7.5.2.1
BuildRequires:    R-CRAN-spatstat >= 1.55.1
BuildRequires:    R-CRAN-PrevMap >= 1.4.1
BuildRequires:    R-CRAN-sp >= 1.2.7
BuildRequires:    R-CRAN-spacetime >= 1.2.2
BuildRequires:    R-Matrix >= 1.2.14
BuildRequires:    R-CRAN-pdist >= 1.2
BuildRequires:    R-CRAN-progress >= 1.1.2
BuildRequires:    R-CRAN-maptools >= 0.9.2
BuildRequires:    R-methods 
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-mapview >= 2.6.0
Requires:         R-CRAN-splancs >= 2.1.40
Requires:         R-CRAN-geoR >= 1.7.5.2.1
Requires:         R-CRAN-spatstat >= 1.55.1
Requires:         R-CRAN-PrevMap >= 1.4.1
Requires:         R-CRAN-sp >= 1.2.7
Requires:         R-CRAN-spacetime >= 1.2.2
Requires:         R-Matrix >= 1.2.14
Requires:         R-CRAN-pdist >= 1.2
Requires:         R-CRAN-progress >= 1.1.2
Requires:         R-CRAN-maptools >= 0.9.2
Requires:         R-methods 

%description
Provides a computationally efficient discrete approximation to
log-Gaussian Cox process model for spatially aggregated disease count
data. It uses Monte Carlo Maximum Likelihood for model parameter
estimation as proposed by Christensen (2004) <doi: 10.1198/106186004X2525>
and delivers prediction of spatially discrete and continuous relative
risk. It performs inference for static spatial and spatio-temporal
dataset. The details of the methods are provided in Johnson et al (2019)
<doi:10.1002/sim.8339>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
