%global packname  BCHM
%global packver   1.00
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.00
Release:          3%{?dist}
Summary:          Clinical Trial Calculation Based on BCHM Design

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-stats 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-rjags 
Requires:         R-stats 
Requires:         R-cluster 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-plyr 

%description
Users can estimate the treatment effect for multiple subgroups basket
trials based on the Bayesian Cluster Hierarchical Model (BCHM). In this
model, a Bayesian non-parametric method is applied to dynamically
calculate the number of clusters by conducting the multiple cluster
classification based on subgroup outcomes. Hierarchical model is used to
compute the posterior probability of treatment effect with the borrowing
strength determined by the Bayesian non-parametric clustering and the
similarities between subgroups. To use this package, 'JAGS' software and
'rjags' package are required, and users need to pre-install them.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
