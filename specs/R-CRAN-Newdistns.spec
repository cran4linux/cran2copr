%global packname  Newdistns
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}
Summary:          Computes Pdf, Cdf, Quantile and Random Numbers, Measures ofInference for 19 General Families of Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AdequacyModel 
Requires:         R-CRAN-AdequacyModel 

%description
Computes the probability density function, cumulative distribution
function, quantile function, random numbers and measures of inference for
the following general families of distributions (each family defined in
terms of an arbitrary cdf G): Marshall Olkin G distributions,
exponentiated G distributions, beta G distributions, gamma G
distributions, Kumaraswamy G distributions, generalized beta G
distributions, beta extended G distributions, gamma G distributions, gamma
uniform G distributions, beta exponential G distributions, Weibull G
distributions, log gamma G I distributions, log gamma G II distributions,
exponentiated generalized G distributions, exponentiated Kumaraswamy G
distributions, geometric exponential Poisson G distributions,
truncated-exponential skew-symmetric G distributions, modified beta G
distributions, and exponentiated exponential Poisson G distributions.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
