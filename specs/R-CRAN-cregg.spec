%global packname  cregg
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Simple Conjoint Tidying, Analysis, and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 3.33
BuildRequires:    R-CRAN-sandwich >= 2.4.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-ggstance 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-survey >= 3.33
Requires:         R-CRAN-sandwich >= 2.4.0
Requires:         R-CRAN-ggplot2 >= 2.0
Requires:         R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-ggstance 
Requires:         R-CRAN-scales 

%description
Simple tidying, analysis, and visualization of conjoint (factorial)
experiments, including estimation and visualization of average marginal
component effects ('AMCEs') and marginal means ('MMs') for weighted and
un-weighted survey data, along with useful reference category diagnostics
and statistical tests. Estimation of 'AMCEs' is based upon methods
described by Hainmueller, Hopkins, and Yamamoto (2014)
<doi:10.1093/pan/mpt024>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
