%global packname  dcemriS4
%global packver   0.55
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.55
Release:          1%{?dist}
Summary:          A Package for Image Analysis of DCE-MRI (S4 Implementation)

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-oro.nifti >= 0.4.3
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-CRAN-oro.nifti >= 0.4.3
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-methods 

%description
A collection of routines and documentation that allows one to perform
voxel-wise quantitative analysis of dynamic contrast-enhanced MRI
(DEC-MRI) and diffusion-weighted imaging (DWI) data, with emphasis on
oncology applications.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/nifti
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
