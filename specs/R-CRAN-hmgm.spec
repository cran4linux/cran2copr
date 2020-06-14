%global packname  hmgm
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          High-Dimensional Mixed Graphical Models Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-nat 
BuildRequires:    R-CRAN-binaryLogic 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-rgl 
Requires:         R-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-MASS 
Requires:         R-CRAN-nat 
Requires:         R-CRAN-binaryLogic 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-methods 

%description
Provides weighted group lasso framework for high-dimensional mixed data
graph estimation. In the graph estimation stage, the graph structure is
estimated by maximizing the conditional likelihood of one variable given
the rest. We focus on the conditional loglikelihood of each variable and
fit separate regressions to estimate the parameters, much in the spirit of
the neighborhood selection approach proposed by Meinshausen-Buhlmann for
the Gaussian Graphical Model and by Ravikumar for the Ising Model.
Currently, the discrete variables can only take two values. In the future,
method for general discrete data and for visualizing the estimated graph
will be added. For more details, see the linked paper.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
