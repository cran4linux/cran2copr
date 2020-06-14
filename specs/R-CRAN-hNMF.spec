%global packname  hNMF
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          2%{?dist}
Summary:          Hierarchical Non-Negative Matrix Factorization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NMF 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-spatialfil 
BuildRequires:    R-CRAN-rasterImage 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
Requires:         R-CRAN-NMF 
Requires:         R-CRAN-oro.nifti 
Requires:         R-tcltk 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-spatialfil 
Requires:         R-CRAN-rasterImage 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 

%description
Hierarchical and single-level non-negative matrix factorization. Several
NMF algorithms are available.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
