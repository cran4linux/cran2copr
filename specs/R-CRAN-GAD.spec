%global __brp_check_rpaths %{nil}
%global packname  GAD
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          GAD: Analysis of variance from general principles

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-R.methodsS3 
Requires:         R-stats 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-R.methodsS3 

%description
This package analyses complex ANOVA models with any combination of
orthogonal/nested and fixed/random factors, as described by Underwood
(1997). There are two restrictions: (i) data must be balanced; (ii) fixed
nested factors are not allowed. Homogeneity of variances is checked using
Cochran's C test and 'a posteriori' comparisons of means are done using
Student-Newman-Keuls (SNK) procedure.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
