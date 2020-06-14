%global packname  leabRa
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          The Artificial Neural Networks Algorithm Leabra

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-R6 >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.4

%description
The algorithm Leabra (local error driven and associative biologically
realistic algorithm) allows for the construction of artificial neural
networks that are biologically realistic and balance supervised and
unsupervised learning within a single framework. This package is based on
the 'MATLAB' version by Sergio Verduzco-Flores, which in turn was based on
the description of the algorithm by Randall O'Reilly (1996)
<ftp://grey.colorado.edu/pub/oreilly/thesis/oreilly_thesis.all.pdf>. For
more general (not 'R' specific) information on the algorithm Leabra see
<https://grey.colorado.edu/emergent/index.php/Leabra>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
