%global packname  PEIP
%global packver   2.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Geophysical Inverse Theory and Optimization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch
BuildRequires:    R-CRAN-bvls 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RSEIS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-bvls 
Requires:         R-Matrix 
Requires:         R-CRAN-RSEIS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-fields 

%description
Several functions introduced in Aster et al.'s book on inverse theory. The
functions are often translations of MATLAB code developed by the authors
to illustrate concepts of inverse theory as applied to geophysics.
Generalized inversion, tomographic inversion algorithms (conjugate
gradients, 'ART' and 'SIRT'), non-linear least squares, first and second
order Tikhonov regularization, roughness constraints, and procedures for
estimating smoothing parameters are included.

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
%{rlibdir}/%{packname}/INDEX
