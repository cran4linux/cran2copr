%global packname  signmedian.test
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          Perform Exact Sign Test and Asymptotic Sign Test in LargeSamples

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Perform sign test on one-sample data, which is one of the oldest
non-parametric statistical methods. Assume that X comes from a continuous
distribution with median = v ( unknown ). Test the null hypothesis H0:
median of X v = mu ( mu is the location parameter and is given in the test
) v.s. the alternative hypothesis H1: v > mu ( or v < mu or v != mu ) and
calculate the p-value. When the sample size is large, perform the
asymptotic sign test. In both ways, calculate the R-estimate of location
of X and the distribution free confidence interval for mu.

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
