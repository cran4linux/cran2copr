%global __brp_check_rpaths %{nil}
%global packname  RevEcoR
%global packver   0.99.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.3
Release:          3%{?dist}%{?buildtag}
Summary:          Reverse Ecology Analysis on Microbiome

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-methods 

%description
An implementation of the reverse ecology framework. Reverse ecology refers
to the use of genomics to study ecology with no a priori assumptions about
the organism(s) under consideration, linking organisms to their
environment. It allows researchers to reconstruct the metabolic networks
and study the ecology of poorly characterized microbial species from their
genomic information, and has substantial potentials for microbial
community ecological analysis.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
