%global packname  spm12r
%global packver   2.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.1
Release:          3%{?dist}
Summary:          Wrapper Functions for 'SPM' (Statistical Parametric Mapping)Version 12 from the 'Wellcome' Trust Centre for 'Neuroimaging'

License:          GPL-2 | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matlabr >= 1.5.2
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-git2r 
Requires:         R-CRAN-matlabr >= 1.5.2
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-neurobase 
Requires:         R-utils 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-git2r 

%description
Installs 'SPM12' to the R library directory and has associated functions
for 'fMRI' and general imaging utilities, called through 'MATLAB'.

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
