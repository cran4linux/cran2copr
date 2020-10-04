%global packname  glinternet
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          3%{?dist}%{?buildtag}
Summary:          Learning Interactions via Hierarchical Group-LassoRegularization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Group-Lasso INTERaction-NET. Fits linear pairwise-interaction models that
satisfy strong hierarchy: if an interaction coefficient is estimated to be
nonzero, then its two associated main effects also have nonzero estimated
coefficients. Accommodates categorical variables (factors) with arbitrary
numbers of levels, continuous variables, and combinations thereof.
Implements the machinery described in the paper "Learning interactions via
hierarchical group-lasso regularization" (JCGS 2015, Volume 24, Issue 3).
Michael Lim & Trevor Hastie (2015) <DOI:10.1080/10618600.2014.938812>.

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
%{rlibdir}/%{packname}/libs
