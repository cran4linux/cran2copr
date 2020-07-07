%global packname  ParBayesianOptimization
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Parallel Bayesian Optimization of Hyperparameters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-CRAN-DiceKriging 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 

%description
Fast, flexible framework for implementing Bayesian optimization of model
hyperparameters according to the methods described in Snoek et al.
<arXiv:1206.2944>. The package allows the user to run scoring function in
parallel, save intermediary results, and tweak other aspects of the
process to fully utilize the computing resources available to the user.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
