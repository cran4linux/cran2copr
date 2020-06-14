%global packname  haploReconstruct
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Reconstruction of Haplotype-Blocks from Time Series Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-gplots 
Requires:         R-stats 
Requires:         R-CRAN-dbscan 
Requires:         R-methods 

%description
Reconstruction of founder haplotype blocks from time series data.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
