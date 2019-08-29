%global packname  mable
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Maximum Approximate Bernstein Likelihood Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
Fit raw or grouped continuous data from a population with a smooth density
on unit interval by an approximate Bernstein polynomial model which is a
mixture of certain beta distributions and find maximum approximate
Bernstein likelihood estimator of the unknown coefficients. Consequently,
maximum likelihood estimates of the unknown density, distribution
functions, and more can be obtained. If the support of the density is not
the unit interval then transformation can be applied. This is an
implementation of the methods proposed by the author this package
published in the Journal of Nonparametric Statistics: Guan (2016)
<doi:10.1080/10485252.2016.1163349> and Guan (2017)
<doi:10.1080/10485252.2017.1374384>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
