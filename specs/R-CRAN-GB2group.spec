%global packname  GB2group
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Estimation of the Generalised Beta Distribution of the SecondKind from Grouped Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GB2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-GB2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-numDeriv 

%description
Estimation of the generalized beta distribution of the second kind (GB2)
and related models using grouped data in form of income shares. The GB2
family is a general class of distributions that provides an accurate fit
to income data. 'GB2group' includes functions to estimate the GB2, the
Singh-Maddala, the Dagum, the Beta 2, the Lognormal and the Fisk
distributions. 'GB2group' deploys two different econometric strategies to
estimate these parametric distributions, non-linear least squares (NLS)
and the generalised method of moments (GMM). Asymptotic standard errors
are reported for the GMM estimates. Standard errors of the NLS estimates
are obtained by Monte Carlo simulation. See Jorda et al. (2018)
<arXiv:1808.09831> for a detailed description of the estimation procedure.

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
