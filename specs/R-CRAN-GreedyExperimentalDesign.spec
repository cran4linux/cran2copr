%global packname  GreedyExperimentalDesign
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Greedy Experimental Design Construction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GreedyExperimentalDesignJARs >= 1.0
BuildRequires:    R-CRAN-rJava >= 0.9.6
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-GreedyExperimentalDesignJARs >= 1.0
Requires:         R-CRAN-rJava >= 0.9.6
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Computes experimental designs for a two-arm experiment with covariates by
greedily optimizing a balance objective function. This optimization
provides lower variance for the treatment effect estimator (and higher
power) while preserving a design that is close to complete randomization.
We return all iterations of the designs for use in a permutation test.
Additional functionality includes using branch and bound optimization (via
Gurobi) and exhaustive enumeration.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
