%global packname  spind
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Methods and Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.49
BuildRequires:    R-CRAN-gee >= 4.13.19
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-splancs >= 2.1.40
BuildRequires:    R-CRAN-rje >= 1.9
BuildRequires:    R-CRAN-waveslim >= 1.7.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-geepack >= 1.2.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-lattice >= 0.20.35
BuildRequires:    R-CRAN-rlang >= 0.2.1
Requires:         R-MASS >= 7.3.49
Requires:         R-CRAN-gee >= 4.13.19
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-splancs >= 2.1.40
Requires:         R-CRAN-rje >= 1.9
Requires:         R-CRAN-waveslim >= 1.7.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-geepack >= 1.2.1
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-lattice >= 0.20.35
Requires:         R-CRAN-rlang >= 0.2.1

%description
Functions for spatial methods based on generalized estimating equations
(GEE) and wavelet-revised methods (WRM), functions for scaling by wavelet
multiresolution regression (WMRR), conducting multi-model inference, and
stepwise model selection. Further, contains functions for spatially
corrected model accuracy measures.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
