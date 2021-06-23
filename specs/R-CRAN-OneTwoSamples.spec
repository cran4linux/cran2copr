%global __brp_check_rpaths %{nil}
%global packname  OneTwoSamples
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Deal with one and two (normal) samples

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
In this package, we introduce an R function one_two_sample() which can
deal with one and two (normal) samples. For one normal sample x, the
function reports descriptive statistics, plot, interval estimation and
test of hypothesis of x. For two normal samples x and y, the function
reports descriptive statistics, plot, interval estimation and test of
hypothesis of x and y, respectively. It also reports interval estimation
and test of hypothesis of mu1-mu2 (the difference of the means of x and y)
and sigma1^2 / sigma2^2 (the ratio of the variances of x and y), tests
whether x and y are from the same population, finds the correlation
coefficient of x and y if x and y have the same length.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
