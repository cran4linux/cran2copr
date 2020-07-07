%global packname  confintr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Confidence Intervals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-boot 
Requires:         R-stats 
Requires:         R-boot 

%description
Calculates classic and/or bootstrap confidence intervals for many
parameters such as the population mean, variance, interquartile range
(IQR), median absolute deviation (MAD), skewness, kurtosis, Cramer's V,
odds ratio, R-squared, quantiles (incl. median), proportions, different
types of correlation measures, difference in means, quantiles and medians.
Many of the classic confidence intervals are described in Smithson, M.
(2003, ISBN: 978-0761924999). Bootstrap confidence intervals are
calculated with the R package 'boot'. Both one- and two-sided intervals
are supported.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
