%global packname  altmeta
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          3%{?dist}
Summary:          Alternative Meta-Analysis Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lme4 
Requires:         R-Matrix 
Requires:         R-CRAN-metafor 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides alternative statistical methods for meta-analysis, including new
heterogeneity tests and measures that are robust to outliers; measures,
tests, and visualization tools for publication bias; meta-analysis methods
for synthesizing proportions; models for multivariate meta-analysis, etc.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
