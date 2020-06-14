%global packname  cifti
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          2%{?dist}
Summary:          Toolbox for Connectivity Informatics Technology Initiative('CIFTI') Files

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-gifti 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-gifti 
Requires:         R-utils 
Requires:         R-CRAN-R.utils 

%description
Functions for the input/output and visualization of medical imaging data
in the form of 'CIFTI' files <https://www.nitrc.org/projects/cifti/>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
