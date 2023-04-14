%global __brp_check_rpaths %{nil}
%global packname  DIRECT
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Clustering of Multivariate Data Under theDirichlet-Process Prior

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
A Bayesian clustering method for replicated time series or replicated
measurements from multiple experimental conditions, e.g., time-course gene
expression data.  It estimates the number of clusters directly from the
data using a Dirichlet-process prior.  See Fu, A. Q., Russell, S., Bray,
S. and Tavare, S. (2013) Bayesian clustering of replicated time-course
gene expression data with weak signals. The Annals of Applied Statistics.
7(3) 1334-1361. <doi:10.1214/13-AOAS650>.

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
