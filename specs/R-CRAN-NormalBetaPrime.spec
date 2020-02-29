%global debug_package %{nil}
%global packname  NormalBetaPrime
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Normal Beta Prime Prior

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-HyperbolicDist 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-HyperbolicDist 

%description
Implements Bayesian linear regression, variable selection, normal means
estimation, and multiple hypothesis testing using the normal-beta prime
prior, as introduced by Bai and Ghosh (2019) <arXiv:1807.02421> and Bai
and Ghosh (2019) <arXiv:1807.06539>. Normal means estimation and multiple
testing for the Dirichlet-Laplace <doi:10.1080/01621459.2014.960967> and
horseshoe+ priors <doi:10.1214/16-BA1028> are also available in this
package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
