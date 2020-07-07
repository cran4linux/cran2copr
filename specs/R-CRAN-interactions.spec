%global packname  interactions
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}
Summary:          Comprehensive, User-Friendly Toolkit for Probing Interactions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jtools >= 2.0.3
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-jtools >= 2.0.3
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 

%description
A suite of functions for conducting and interpreting analysis of
statistical interaction in regression models that was formerly part of the
'jtools' package. Functionality includes visualization of two- and
three-way interactions among continuous and/or categorical variables as
well as calculation of "simple slopes" and Johnson-Neyman intervals (see
e.g., Bauer & Curran, 2005 <doi:10.1207/s15327906mbr4003_5>). These
capabilities are implemented for generalized linear models in addition to
the standard linear regression context.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
