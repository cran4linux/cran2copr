%global packname  phenesse
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Estimate Phenological Metrics using Presence-Only Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-stats 
Requires:         R-boot 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-stats 

%description
Generates Weibull-parameterized estimates of phenology for any percentile
of a distribution using the framework established in Cooke (1979)
<doi:10.1093/biomet/66.2.367>.. Extensive testing against other estimators
suggest the weib_percentile() function is especially useful in generating
more accurate and less biased estimates of onset and offset.
Non-parametric bootstrapping can be used to generate confidence intervals
around those estimates. Additionally, this package offers an easy way to
perform non-parametric bootstrapping to generate confidence intervals for
quantile estimates, mean estimates, or any statistical function of
interest.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
