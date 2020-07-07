%global packname  bcTSNE
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          3%{?dist}
Summary:          Projected t-SNE for Batch Correction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-RSpectra 
Requires:         R-utils 
Requires:         R-CRAN-Rtsne 
Requires:         R-graphics 

%description
Implements the projected t-SNE method for batch correction of
high-dimensional data. Please see Aliverti et al. (2020)
<doi:10.1093/bioinformatics/btaa189> for more information.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/realDataAnalysis.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
