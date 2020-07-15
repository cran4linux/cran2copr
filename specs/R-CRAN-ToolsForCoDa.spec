%global packname  ToolsForCoDa
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}
Summary:          Multivariate Tools for Compositional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-calibrate 
BuildRequires:    R-CRAN-robCompositions 
Requires:         R-MASS 
Requires:         R-CRAN-calibrate 
Requires:         R-CRAN-robCompositions 

%description
Provides functions for multivariate analysis with compositional data.
Includes a function for doing compositional canonical correlation
analysis.  This analysis requires two data matrices of compositions, which
can be adequately transformed and used as entries in a specialized program
for canonical correlation analysis, that is able to deal with singular
covariance matrices. The methodology is described in Graffelman et al.
(2017) <doi:10.1101/144584>. A function for log-ratio principal component
analysis with condition number computations has been added to the package.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
