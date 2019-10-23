%global packname  qtlcharts
%global packver   0.11-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.6
Release:          1%{?dist}
Summary:          Interactive Graphics for QTL Experiments

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-qtl >= 1.30.4
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-qtl >= 1.30.4
Requires:         R-CRAN-htmlwidgets 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Web-based interactive charts (using D3.js) for the analysis of
experimental crosses to identify genetic loci (quantitative trait loci,
QTL) contributing to variation in quantitative traits.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/htmlwidgets
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
