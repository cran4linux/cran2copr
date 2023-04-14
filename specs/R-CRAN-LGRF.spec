%global __brp_check_rpaths %{nil}
%global packname  LGRF
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Set-Based Tests for Genetic Association in Longitudinal Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-SKAT 
BuildRequires:    R-CRAN-geepack 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-SKAT 
Requires:         R-CRAN-geepack 

%description
Functions for the longitudinal genetic random field method (He et al.,
2015, <doi:10.1111/biom.12310>) to test the association between a
longitudinally measured quantitative outcome and a set of genetic variants
in a gene/region.

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
