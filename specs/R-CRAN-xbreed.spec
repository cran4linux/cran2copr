%global __brp_check_rpaths %{nil}
%global packname  xbreed
%global packver   1.0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Genomic Simulation of Purebred and Crossbred Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BGLR 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-BGLR 

%description
Simulation of purebred and crossbred genomic data as well as pedigree and
phenotypes are possible by this package. 'xbreed' can be used for the
simulation of populations with flexible genome structures and trait
genetic architectures. It can also be used to evaluate breeding schemes
and generate genetic data to test statistical tools.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
