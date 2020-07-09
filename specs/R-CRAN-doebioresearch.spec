%global packname  doebioresearch
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Analysis of Design of Experiments for Biological Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-CRAN-agricolae >= 1.3.3
Requires:         R-stats >= 4.0.2
Requires:         R-CRAN-agricolae >= 1.3.3

%description
Performs analysis of popular experimental designs used in the field of
biological research. The designs covered are completely randomized design,
randomized complete block design, factorial completely randomized design,
factorial randomized complete block design, split plot design, strip plot
design and latin square design. The analysis include analysis of variance,
coefficient of determination, normality test of residuals, standard error
of mean, standard error of difference and multiple comparison test of
means. The package has functions for transformation of data and yield data
conversion. Some datasets are also added in order to facilitate examples.

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
