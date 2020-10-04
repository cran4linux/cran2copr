%global packname  clusterGeneration
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          3%{?dist}%{?buildtag}
Summary:          Random Cluster Generation (with Specified Degree of Separation)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.1
Requires:         R-core >= 2.9.1
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
We developed the clusterGeneration package to provide functions for
generating random clusters, generating random covariance/correlation
matrices, calculating a separation index (data and population version) for
pairs of clusters or cluster distributions, and 1-D and 2-D projection
plots to visualize clusters.  The package also contains a function to
generate random clusters based on factorial designs with factors such as
degree of separation, number of clusters, number of variables, number of
noisy variables.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
