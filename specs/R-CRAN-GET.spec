%global packname  GET
%global packver   0.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          3%{?dist}
Summary:          Global Envelopes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-spatstat 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of global envelopes for a set of general d-dimensional
vectors T in various applications. A 100(1-alpha)% global envelope is a
band bounded by two vectors such that the probability that T falls outside
this envelope in any of the d points is equal to alpha. Global means that
the probability is controlled simultaneously for all the d elements of the
vectors. The global envelopes can be used for graphical Monte Carlo and
permutation tests where the test statistic is a multivariate vector or
function (e.g. goodness-of-fit testing for point patterns and random sets,
functional analysis of variance, functional general linear model, n-sample
test of correspondence of distribution functions), for central regions of
functional or multivariate data (e.g. outlier detection, functional
boxplot) and for global confidence and prediction bands (e.g. confidence
band in polynomial regression, Bayesian posterior prediction). See
Myllymäki and Mrkvička (2019) <arXiv:1911.06583>, Myllymäki et al. (2017)
<doi: 10.1111/rssb.12172>, Mrkvička et al. (2017) <doi:
10.1007/s11222-016-9683-9>, Mrkvička et al. (2016) <doi:
10.1016/j.spasta.2016.04.005>, Mrkvička et al. (2018) <arXiv:1612.03608>,
Mrkvička et al. (2019) <arXiv:1906.09004>, Mrkvička et al. (2019)
<arXiv:1902.04926>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
