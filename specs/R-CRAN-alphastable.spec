%global packname  alphastable
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Inference for Stable Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-stabledist 
BuildRequires:    R-nlme 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-stabledist 
Requires:         R-nlme 

%description
Developed to perform the tasks given by the following. 1-computing the
probability density function and distribution function of a univariate
stable distribution; 2- generating from univariate stable, truncated
stable, multivariate elliptically contoured stable, and bivariate strictly
stable distributions; 3- estimating the parameters of univariate symmetric
stable, skew stable, Cauchy, multivariate elliptically contoured stable,
and multivariate strictly stable distributions; 4- estimating the
parameters of the mixture of symmetric stable and mixture of Cauchy
distributions.

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
