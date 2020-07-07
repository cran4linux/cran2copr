%global packname  SCBiclust
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Identifies Mean, Variance, and Hierarchically ClusteredBiclusters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sparcl 
BuildRequires:    R-CRAN-sigclust 
Requires:         R-CRAN-sparcl 
Requires:         R-CRAN-sigclust 

%description
Identifies a bicluster, a submatrix of the data such that the features and
observations within the submatrix differ from those not contained in
submatrix, using a two-step method. In the first step, observations in the
bicluster are identified to maximize the sum of weighted between cluster
feature differences. The observations are identified in a similar fashion
as in Witten and Tibshirani (2010) <doi:10.1198/jasa.2010.tm09415> except
with a modified objective function and no feature sparsity constraint. In
the second step, features in the bicluster are identified based on their
contribution to the clustering of the observations. The cluster
significance test of Liu, Hayes, Nobel, and Marron (2008):
<doi:10.1198/016214508000000454> can then be used to test the strength of
the identified bicluster. 'SCBiclust' can be used to identify biclusters
which differ based on feature means, feature variances, or more general
differences.

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
%{rlibdir}/%{packname}/INDEX
