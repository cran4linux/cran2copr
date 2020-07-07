%global packname  rARPACK
%global packver   0.11-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.0
Release:          3%{?dist}
Summary:          Solvers for Large Scale Eigenvalue and SVD Problems

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-RSpectra 

%description
Previously an R wrapper of the 'ARPACK' library
<http://www.caam.rice.edu/software/ARPACK/>, and now a shell of the R
package 'RSpectra', an R interface to the 'Spectra' library
<http://yixuan.cos.name/spectra/> for solving large scale
eigenvalue/vector problems. The current version of 'rARPACK' simply
imports and exports the functions provided by 'RSpectra'. New users of
'rARPACK' are advised to switch to the 'RSpectra' package.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
