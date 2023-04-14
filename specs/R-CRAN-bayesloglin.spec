%global __brp_check_rpaths %{nil}
%global packname  bayesloglin
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Contingency Table Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
The function MC3() searches for log-linear models with the highest
posterior probability. The function gibbsSampler() is a blocked Gibbs
sampler for sampling from the posterior distribution of the log-linear
parameters. The functions findPostMean() and findPostCov() compute the
posterior mean and covariance matrix for decomposable models which, for
these models, is available in closed form.

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
