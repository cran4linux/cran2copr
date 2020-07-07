%global packname  kamila
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Methods for Clustering Mixed-Type Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-abind 
Requires:         R-KernSmooth 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-plyr 

%description
Implements methods for clustering mixed-type data, specifically
combinations of continuous and nominal data. Special attention is paid to
the often-overlooked problem of equitably balancing the contribution of
the continuous and categorical variables. This package implements KAMILA
clustering, a novel method for clustering mixed-type data in the spirit of
k-means clustering. It does not require dummy coding of variables, and is
efficient enough to scale to rather large data sets. Also implemented is
Modha-Spangler clustering, which uses a brute-force strategy to maximize
the cluster separation simultaneously in the continuous and categorical
variables. For more information, see Foss, Markatou, Ray, & Heching (2016)
<doi:10.1007/s10994-016-5575-7> and Foss & Markatou (2018)
<doi:10.18637/jss.v083.i13>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
