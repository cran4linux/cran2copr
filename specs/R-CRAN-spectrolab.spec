%global packname  spectrolab
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          3%{?dist}
Summary:          Class and Methods for Hyperspectral Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-prospectr 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-usethis 
Requires:         R-stats 
Requires:         R-CRAN-prospectr 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-usethis 

%description
Input/Output, processing and visualization of spectra taken with different
spectrometers, including SVC (Spectra Vista), ASD and PSR (Spectral
Evolution). Implements an S3 class 'spectra' that other packages can build
on. Provides methods to access, plot, manipulate, splice sensor overlap,
vector normalize and smooth spectra.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
