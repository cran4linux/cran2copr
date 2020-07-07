%global packname  codyn
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}
Summary:          Community Dynamics Metrics

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-assertthat 
Requires:         R-stats 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-vegan 

%description
Univariate and multivariate temporal and spatial diversity indices, rank
abundance curves, and community stability measures. The functions
implement measures that are either explicitly temporal and include the
option to calculate them over multiple replicates, or spatial and include
the option to calculate them over multiple time points. Functions fall
into five categories: static diversity indices, temporal diversity
indices, spatial diversity indices, rank abundance curves, and community
stability measures. The diversity indices are temporal and spatial analogs
to traditional diversity indices. Specifically, the package includes
functions to calculate community richness, evenness and diversity at a
given point in space and time. In addition, it contains functions to
calculate species turnover, mean rank shifts, and lags in community
similarity between two time points.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
