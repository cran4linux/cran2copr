%global packname  laGP
%global packver   1.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}
Summary:          Local Approximate Gaussian Process Regression

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-parallel 
Requires:         R-CRAN-tgp 
Requires:         R-parallel 

%description
Performs approximate GP regression for large computer experiments and
spatial datasets.  The approximation is based on finding small local
designs for prediction (independently) at particular inputs. OpenMP and
SNOW parallelization are supported for prediction over a vast
out-of-sample testing set; GPU acceleration is also supported for an
important subroutine.  OpenMP and GPU features may require special
compilation.  An interface to lower-level (full) GP inference and
prediction is provided. Wrapper routines for blackbox optimization under
mixed equality and inequality constraints via an augmented Lagrangian
scheme, and for large scale computer model calibration, are also provided.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
