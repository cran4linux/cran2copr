%global packname  calibrator
%global packver   1.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          2%{?dist}
Summary:          Bayesian Calibration of Complex Computer Codes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-emulator >= 1.2.11
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-cubature 
Requires:         R-CRAN-emulator >= 1.2.11
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-cubature 

%description
Performs Bayesian calibration of computer models as per Kennedy and
O'Hagan 2001.  The package includes routines to find the hyperparameters
and parameters; see the help page for stage1() for a worked example using
the toy dataset.  A tutorial is provided in the calex.Rnw vignette; and a
suite of especially simple one dimensional examples appears in
inst/doc/one.dim/.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
