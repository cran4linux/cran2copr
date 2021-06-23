%global __brp_check_rpaths %{nil}
%global packname  DEMOVA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          DEvelopment (of Multi-Linear QSPR/QSAR) MOdels VAlidated usingTest Set

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-leaps 
Requires:         R-CRAN-leaps 

%description
Tool for the development of multi-linear QSPR/QSAR models (Quantitative
structure-property/activity relationship). Theses models are used in
chemistry, biology and pharmacy to find a relationship between the
structure of a molecule and its property (such as activity, toxicology but
also physical properties). The various functions of this package allows:
selection of descriptors based of variances, intercorrelation and user
expertise; selection of the best multi-linear regression in terms of
correlation and robustness; methods of internal validation (Leave-One-Out,
Leave-Many-Out, Y-scrambling) and external using test sets.

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
%{rlibdir}/%{packname}/INDEX
