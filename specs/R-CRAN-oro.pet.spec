%global packname  oro.pet
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          Rigorous - Positron Emission Tomography

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-oro.dicom >= 0.4.0
BuildRequires:    R-CRAN-oro.nifti >= 0.4.0
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-msm 
Requires:         R-CRAN-oro.dicom >= 0.4.0
Requires:         R-CRAN-oro.nifti >= 0.4.0
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-msm 

%description
Image analysis techniques for positron emission tomography (PET) that form
part of the Rigorous Analytics bundle.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
