%global packname  libamtrack
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}
Summary:          Computational Routines for Proton and Ion Radiotherapy

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel >= 1.8
Requires:         gsl
BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0

%description
R interface to the open-source, ANSI C library 'libamtrack'
(http://libamtrack.dkfz.org). 'libamtrack' provides computational routines
for the prediction of detector response and radiobiological efficiency in
heavy charged particle beams. It is designed for research in proton and
ion dosimetry and radiotherapy. 'libamtrack' also includes many auxiliary
physics routines for proton and ion beams. Original package and C-to-R
conversion routines developed by Felix A. Klein.

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
%{rlibdir}/%{packname}/libs
