%global __brp_check_rpaths %{nil}
%global packname  BBI
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Benthic Biotic Indices Calculation from Composition Data

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-vegan 

%description
Set of functions to calculate Benthic Biotic Indices from composition
data, obtained whether from morphotaxonomic inventories or sequencing
data. Based on reference ecological weights publicly available for a set
of commonly used marine biotic indices, such as AMBI (A Marine Biotic
Index, Borja et al., 2000) <doi:10.1016/S0025-326X(00)00061-8> NSI
(Norwegian Sensitivity Index) and ISI (Indicator Species Index) (Rygg
2013, <ISBN:978-82-577-6210-0>). It provides the ecological quality status
of the samples based on each BBI as well as the normalized Ecological
Quality Ratio.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/TABLE_REF.Rd
%{rlibdir}/%{packname}/INDEX
