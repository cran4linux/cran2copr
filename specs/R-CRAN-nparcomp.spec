%global packname  nparcomp
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}
Summary:          Multiple Comparisons and Simultaneous Confidence Intervals

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-mvtnorm 

%description
With this package, it is possible to compute nonparametric simultaneous
confidence intervals for relative contrast effects in the unbalanced one
way layout. Moreover, it computes simultaneous p-values. The simultaneous
confidence intervals can be computed using multivariate normal
distribution, multivariate t-distribution with a Satterthwaite
Approximation of the degree of freedom or using multivariate range
preserving transformations with Logit or Probit as transformation
function. 2 sample comparisons can be performed with the same methods
described above. There is no assumption on the underlying distribution
function, only that the data have to be at least ordinal numbers. See
Konietschke et al. (2015) <doi:10.18637/jss.v064.i09> for details.

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
%{rlibdir}/%{packname}/INDEX
