%global __brp_check_rpaths %{nil}
%global packname  FSTpackage
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Unified Sequence-Based Association Tests Allowing for MultipleFunctional Annotation Scores

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-SKAT 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-SKAT 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Functions for sequencing studies allowing for multiple functional
annotation scores. Score type tests and an efficient perturbation method
are used for individual gene/large gene-set/genome wide analysis. Only
summary statistics are needed.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
