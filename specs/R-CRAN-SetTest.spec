%global packname  SetTest
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Group Testing Procedures for Signal Detection andGoodness-of-Fit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
It provides cumulative distribution function (CDF), quantile, p-value,
statistical power calculator and random number generator for a collection
of group-testing procedures, including the Higher Criticism tests, the
one-sided Kolmogorov-Smirnov tests, the one-sided Berk-Jones tests, the
one-sided phi-divergence tests, etc. The input are a group of p-values.
The null hypothesis is that they are i.i.d. Uniform(0,1). In the context
of signal detection, the null hypothesis means no signals. In the context
of the goodness-of-fit testing, which contrasts a group of i.i.d. random
variables to a given continuous distribution, the input p-values can be
obtained by the CDF transformation. The null hypothesis means that these
random variables follow the given distribution. For reference, see Hong
Zhang, Jiashun Jin and Zheyang Wu. "Distributions and Statistical Power of
Optimal Signal-Detection Methods In Finite Cases", submitted.

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
