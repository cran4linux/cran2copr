%global __brp_check_rpaths %{nil}
%global packname  spatialClust
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Clustering using Fuzzy Geographically WeightedClustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-CRAN-maptools >= 0.8.37
BuildRequires:    R-CRAN-rgeos >= 0.3.15
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-CRAN-maptools >= 0.8.37
Requires:         R-CRAN-rgeos >= 0.3.15

%description
Perform Spatial Clustering Analysis using Fuzzy Geographically Weighted
Clustering. Provide optimization using Gravitational Search Algorithm.

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
%{rlibdir}/%{packname}/INDEX
