%global __brp_check_rpaths %{nil}
%global packname  ktaucenters
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Clustering Procedures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-GSE 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbscan 
Requires:         R-stats 
Requires:         R-CRAN-GSE 

%description
A clustering algorithm similar to K-Means is implemented, it has two main
advantages, namely (a) The estimator is resistant to outliers, that means
that results of estimator are still correct when there are atypical values
in the sample and (b) The estimator is efficient, roughly speaking, if
there are no outliers in the sample, results will be similar than those
obtained by a classic algorithm (K-Means). Clustering procedure is carried
out by minimizing the overall robust scale so-called tau scale. (see
Gonzalez, Yohai and Zamar (2019) <arxiv:1906.08198>).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
