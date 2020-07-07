%global packname  CISE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Common and Individual Structure Explained for Multiple Graphs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 2.0.13
BuildRequires:    R-Matrix >= 1.2.12
BuildRequires:    R-CRAN-rARPACK >= 0.11.0
BuildRequires:    R-CRAN-far 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-MASS 
Requires:         R-CRAN-glmnet >= 2.0.13
Requires:         R-Matrix >= 1.2.12
Requires:         R-CRAN-rARPACK >= 0.11.0
Requires:         R-CRAN-far 
Requires:         R-CRAN-gdata 
Requires:         R-MASS 

%description
Specific dimension reduction methods for replicated graphs (multiple
undirected graphs repeatedly measured on a common set of nodes). The
package contains efficient procedures for estimating a shared baseline
propensity matrix and graph-specific low rank matrices. The algorithm uses
block coordinate descent algorithm to solve the model, which alternatively
performs L2-penalized logistic regression and multiple partial eigenvalue
decompositions, as described in the paper Wang et al. (2017)
<arXiv:1707.06360>.

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
%{rlibdir}/%{packname}/INDEX
