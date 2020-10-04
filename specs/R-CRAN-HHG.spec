%global packname  HHG
%global packver   2.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Heller-Heller-Gorfine Tests of Independence and Equality ofDistributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-Rcpp >= 0.12.9

%description
Heller-Heller-Gorfine tests are a set of powerful statistical tests of
multivariate k-sample homogeneity and independence (Heller et. al., 2013,
<doi:10.1093/biomet/ass070>). For the univariate case, the package also
offers implementations of the 'MinP DDP' and 'MinP ADP' tests by Heller
et. al. (2016), which are consistent against all continuous alternatives
but are distribution-free, and are thus much faster to apply.

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
%{rlibdir}/%{packname}/libs
