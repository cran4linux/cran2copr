%global packname  fslr
%global packver   2.24.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.24.1
Release:          2%{?dist}
Summary:          Wrapper Functions for 'FSL' ('FMRIB' Software Library) fromFunctional MRI of the Brain ('FMRIB')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-oro.nifti >= 0.5.0
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-oro.nifti >= 0.5.0
Requires:         R-CRAN-neurobase 
Requires:         R-methods 
Requires:         R-CRAN-R.utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Wrapper functions that interface with 'FSL'
<http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>, a powerful and commonly-used
'neuroimaging' software, using system commands. The goal is to be able to
interface with 'FSL' completely in R, where you pass R objects of class
'nifti', implemented by package 'oro.nifti', and the function executes an
'FSL' command and returns an R object of class 'nifti' if desired.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
