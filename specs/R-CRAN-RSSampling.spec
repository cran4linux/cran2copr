%global packname  RSSampling
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Ranked Set Sampling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-LearnBayes 
BuildRequires:    R-stats 
Requires:         R-CRAN-LearnBayes 
Requires:         R-stats 

%description
Ranked set sampling (RSS) is introduced as an advanced method for data
collection which is substantial for the statistical and methodological
analysis in scientific studies by McIntyre (1952) (reprinted in 2005)
<doi:10.1198/000313005X54180>. This package introduces the first package
that implements the RSS and its modified versions for sampling. With
'RSSampling', the researchers can sample with basic RSS and the modified
versions, namely, Median RSS, Extreme RSS, Percentile RSS, Balanced groups
RSS, Double RSS, L-RSS, Truncation-based RSS, Robust extreme RSS. The
'RSSampling' also allows imperfect ranking using an auxiliary variable
(concomitant) which is widely used in the real life applications.
Applicants can also use this package for parametric and nonparametric
inference such as mean, median and variance estimation, regression
analysis and some distribution-free tests where the the samples are
obtained via basic RSS.

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
