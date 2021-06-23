%global __brp_check_rpaths %{nil}
%global packname  CommT
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Comparative Phylogeographic Analysis using the Community TreeFramework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 3.1.4
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-ape >= 3.1.4
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-reshape 

%description
Provides functions to measure the difference between constrained and
unconstrained gene tree distributions using various tree distance metrics.
Constraints are enforced prior to this analysis via the estimation of a
tree under the community tree model.

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
%{rlibdir}/%{packname}/INDEX
