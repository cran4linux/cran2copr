%global packname  blink
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Record Linkage for Empirically Motivated Priors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-RecordLinkage 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-RecordLinkage 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-utils 

%description
An implementation of the model in Steorts (2015) <DOI:10.1214/15-BA965SI>,
which performs Bayesian entity resolution for categorical and text data,
for any distance function defined by the user. In addition, the precision
and recall are in the package to allow one to compare to any other
comparable method such as logistic regression, Bayesian additive
regression trees (BART), or random forests. The experiments are
reproducible and illustrated using a simple vignette. LICENSE: GPL-3 +
file license.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
