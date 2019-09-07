%global packname  spatialwarnings
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Spatial Early Warning Signals of Ecosystem Degradation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 

%description
Tools to compute and assess significance of early-warnings signals (EWS)
of ecosystem degradation on raster data sets. EWS are metrics derived from
the observed spatial structure of an ecosystem -- e.g. spatial
autocorrelation -- that increase before an ecosystem undergoes a
non-linear transition (Genin et al. (2018) <doi:10.1111/2041-210X.13058>).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
