%global packname  tractor.base
%global packver   3.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.2
Release:          2%{?dist}
Summary:          Read, Manipulate and Visualise Magnetic Resonance Images

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ore >= 1.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reportr 
BuildRequires:    R-CRAN-shades 
BuildRequires:    R-CRAN-RNifti 
Requires:         R-CRAN-ore >= 1.3.0
Requires:         R-methods 
Requires:         R-CRAN-reportr 
Requires:         R-CRAN-shades 
Requires:         R-CRAN-RNifti 

%description
Functions for working with magnetic resonance images. Reading and writing
of popular file formats (DICOM, Analyze, NIfTI-1, NIfTI-2, MGH);
interactive and non-interactive visualisation; flexible image
manipulation; metadata and sparse image handling.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
