%global packname  ClimProjDiags
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Set of Tools to Compute Various Climate Indices

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiApply >= 2.0.0
BuildRequires:    R-CRAN-PCICt 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-multiApply >= 2.0.0
Requires:         R-CRAN-PCICt 
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
Set of tools to compute metrics and indices for climate analysis. The
package provides functions to compute extreme indices, evaluate the
agreement between models and combine theses models into an ensemble.
Multi-model time series of climate indices can be computed either after
averaging the 2-D fields from different models provided they share a
common grid or by combining time series computed on the model native grid.
Indices can be assigned weights and/or combined to construct new indices.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
