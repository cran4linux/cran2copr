%global packname  ReliabilityTheory
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Tools for Structural Reliability Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-PhaseType >= 0.1.3
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-FRACTION 
BuildRequires:    R-CRAN-mcmc 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-HI 
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-PhaseType >= 0.1.3
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-FRACTION 
Requires:         R-CRAN-mcmc 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-HI 

%description
A variety of tools useful for performing structural reliability analysis,
such as with structure function and system signatures.  Plans to expand
more widely.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
