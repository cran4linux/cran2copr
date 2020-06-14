%global packname  GroupBN
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Learn Group Bayesian Networks using Hierarchical Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-ClustOfVar 
BuildRequires:    R-CRAN-PCAmixdata 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-ClustOfVar 
Requires:         R-CRAN-PCAmixdata 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-PRROC 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-rlist 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 

%description
Learn group Bayesian Networks using hierarchical Clustering. This package
implements the inference of group Bayesian networks based on hierarchical
Clustering, and the adaptive refinement of the grouping regarding an
outcome of interest.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
