%global packname  pgraph
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}
Summary:          Build Dependency Graphs using Projection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SAM 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-splines 
Requires:         R-CRAN-SAM 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-glmnet 
Requires:         R-splines 

%description
Implements a general framework for creating dependency graphs using
projection as introduced in Fan, Feng and Xia (2019)<arXiv:1501.01617>.
Both lasso and sparse additive model projections are implemented. Both
Pearson correlation and distance covariance options are available to
generate the graph.

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
