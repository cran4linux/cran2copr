%global __brp_check_rpaths %{nil}
%global packname  LCF
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          3%{?dist}%{?buildtag}
Summary:          Linear Combination Fitting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-quadprog 

%description
Baseline correction, normalization and linear combination fitting (LCF) of
X-ray absorption near edge structure (XANES) spectra. The package includes
data loading of .xmu files exported from 'ATHENA' (Ravel and Newville,
2005) <doi:10.1107/S0909049505012719>. Loaded spectra can be background
corrected and all standards can be fitted at once. Two linear combination
fitting functions can be used: (1) fit_athena(): Simply fitting
combinations of standards as in ATHENA, (2) fit_float(): Fitting all
standards with changing baseline correction and edge-step normalization
parameters.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
