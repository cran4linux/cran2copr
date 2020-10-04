%global packname  Metatron
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Meta-analysis for Classification Data and Correction toImperfect Reference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mpt 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mpt 
Requires:         R-Matrix 

%description
This package allows doing meta-analysis for primary studies with
classification outcomes in order to evaluate systematically the accuracies
of classifiers, namely, the diagnostic tests. It provides functions to fit
the bivariate model of Reitsma et al.(2005). Moreover, if the reference
employed in the classification process isn't a gold standard, its deficit
can be detected and its influence to the underestimation of the diagnostic
test's accuracy can be corrected, as described in Botella et al.(2013).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
