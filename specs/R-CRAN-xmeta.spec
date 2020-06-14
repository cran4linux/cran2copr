%global packname  xmeta
%global packver   1.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          2%{?dist}
Summary:          A Toolbox for Multivariate Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-glmmML 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-mvmeta 
BuildRequires:    R-stats 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-glmmML 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-mvmeta 
Requires:         R-stats 

%description
A toolbox for meta-analysis. This package includes a collection of
functions for (1) implementing robust multivariate meta-analysis of
continuous or binary outcomes; and (2) a bivariate Egger's test for
detecting small study effects.

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
