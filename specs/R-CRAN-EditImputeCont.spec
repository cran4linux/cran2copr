%global packname  EditImputeCont
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Simultaneous Edit-Imputation for Continuous Microdata

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-editrules 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-editrules 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-igraph 

%description
An integrated editing and imputation method for continuous microdata under
linear constraints is implemented. It relies on a Bayesian nonparametric
hierarchical modeling approach as described in Kim et al. (2015)
<doi:10.1080/01621459.2015.1040881>. In this approach, the joint
distribution of the data is estimated by a flexible joint probability
model. The generated edit-imputed data are guaranteed to satisfy all
imposed edit rules, whose types include ratio edits, balance edits and
range restrictions.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
