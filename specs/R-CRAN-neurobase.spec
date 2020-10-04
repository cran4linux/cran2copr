%global packname  neurobase
%global packver   1.29.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.29.0
Release:          3%{?dist}%{?buildtag}
Summary:          'Neuroconductor' Base Package with Helper Functions for 'nifti'Objects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-oro.nifti >= 0.9.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RNifti 
Requires:         R-CRAN-oro.nifti >= 0.9.0
Requires:         R-methods 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-R.utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-RNifti 

%description
Base package for 'Neuroconductor', which includes many helper functions
that interact with objects of class 'nifti', implemented by package
'oro.nifti', for reading/writing and also other manipulation functions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
