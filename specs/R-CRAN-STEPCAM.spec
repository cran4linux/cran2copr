%global packname  STEPCAM
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          ABC-SMC Inference of STEPCAM

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-FD 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-ade4 
Requires:         R-grid 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-ape 

%description
Collection of model estimation, and model plotting functions related to
the STEPCAM family of community assembly models. STEPCAM is a STEPwise
Community Assembly Model that infers the relative contribution of
Dispersal Assembly, Habitat Filtering and Limiting Similarity from a
dataset consisting of the combination of trait and abundance data. See
also <http://onlinelibrary.wiley.com/wol1/doi/10.1890/14-0454.1/abstract>
for more information.

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
