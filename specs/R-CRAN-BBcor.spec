%global packname  BBcor
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Bayesian Bootstrapping Correlations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-psych >= 1.9.12.31
BuildRequires:    R-CRAN-pbapply >= 1.4.2
BuildRequires:    R-CRAN-wdm >= 0.2.1
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-psych >= 1.9.12.31
Requires:         R-CRAN-pbapply >= 1.4.2
Requires:         R-CRAN-wdm >= 0.2.1
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Efficiently draw samples from the posterior distribution of various
correlation coefficients with the Bayesian bootstrap described in Rubin
(1981) <doi:10.1214/aos/1176345338>. There are five correlation
coefficients, including Pearson, Kendall, Spearman, Blomqvist, and
polychoric.

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
