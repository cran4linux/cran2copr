%global __brp_check_rpaths %{nil}
%global packname  sda
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          3%{?dist}%{?buildtag}
Summary:          Shrinkage Discriminant Analysis and CAT Score Variable Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.8
BuildRequires:    R-CRAN-fdrtool >= 1.2.15
BuildRequires:    R-CRAN-entropy >= 1.2.1
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-corpcor >= 1.6.8
Requires:         R-CRAN-fdrtool >= 1.2.15
Requires:         R-CRAN-entropy >= 1.2.1
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides an efficient framework for high-dimensional linear and diagonal
discriminant analysis with variable selection.  The classifier is trained
using James-Stein-type shrinkage estimators and predictor variables are
ranked using correlation-adjusted t-scores (CAT scores).  Variable
selection error is controlled using false non-discovery rates or higher
criticism.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
