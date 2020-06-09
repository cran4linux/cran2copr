%global packname  oro.nifti
%global packver   0.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.3
Release:          1%{?dist}
Summary:          Rigorous - 'NIfTI' + 'ANALYZE' + 'AFNI' : Input / Output

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RNifti >= 0.9.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-rticles 
Requires:         R-CRAN-RNifti >= 0.9.0
Requires:         R-stats 
Requires:         R-CRAN-bitops 
Requires:         R-splines 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-rticles 

%description
Functions for the input/output and visualization of medical imaging data
that follow either the 'ANALYZE', 'NIfTI' or 'AFNI' formats.  This package
is part of the Rigorous Analytics bundle.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/afni
%doc %{rlibdir}/%{packname}/anlz
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/nifti
%{rlibdir}/%{packname}/INDEX
