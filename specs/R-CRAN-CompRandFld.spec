%global packname  CompRandFld
%global packver   1.0.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3.5
Release:          1%{?dist}
Summary:          Composite-Likelihood Based Analysis of Random Fields

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13
Requires:         R-core >= 2.13
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-mapproj 
Requires:         R-methods 
Requires:         R-CRAN-maps 

%description
A set of procedures for the analysis of Random Fields using likelihood and
non-standard likelihood methods is provided. Spatial analysis often
involves dealing with large dataset. Therefore even simple studies may be
too computationally demanding. Composite likelihood inference is emerging
as a useful tool for mitigating such computational problems. This
methodology shows satisfactory results when compared with other techniques
such as the tapering method. Moreover, composite likelihood (and related
quantities) have some useful properties similar to those of the standard
likelihood.

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
%{rlibdir}/%{packname}/libs
