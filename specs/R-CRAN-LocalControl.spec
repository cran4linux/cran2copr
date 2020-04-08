%global packname  LocalControl
%global packver   1.1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2.1
Release:          1%{?dist}
Summary:          Nonparametric Methods for Generating High Quality ComparativeEffectiveness Evidence

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gss 
BuildRequires:    R-cluster 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gss 
Requires:         R-cluster 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements novel nonparametric approaches to address biases and
confounding when comparing treatments or exposures in observational
studies of outcomes. While designed and appropriate for use in studies
involving medicine and the life sciences, the package can be used in other
situations involving outcomes with multiple confounders. The package
implements a family of methods for non-parametric bias correction when
comparing treatments in observational studies, including survival analysis
settings, where competing risks and/or censoring may be present. The
approach extends to bias-corrected personalized predictions of treatment
outcome differences, and analysis of heterogeneity of treatment
effect-sizes across patient subgroups.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
