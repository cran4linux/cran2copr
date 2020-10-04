%global packname  klaR
%global packver   0.6-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.15
Release:          3%{?dist}%{?buildtag}
Summary:          Classification and Visualization

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-questionr 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-questionr 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Miscellaneous functions for classification and visualization, e.g.
regularized discriminant analysis, sknn() kernel-density naive Bayes, an
interface to 'svmlight' and stepclass() wrapper variable selection for
supervised classification, partimat() visualization of classification
rules and shardsplot() of cluster results as well as kmodes() clustering
for categorical data, corclust() variable clustering, variable extraction
from different variable clustering models and weight of evidence
preprocessing.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
