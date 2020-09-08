%global packname  bootComb
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Combine Parameter Estimates via Parametric Bootstrap

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Propagate uncertainty from several estimates when combining these
estimates via a function. This is done by using the parametric bootstrap
to simulate values from the distribution of each estimate to build up an
empirical distribution of the combined parameter. Finally either the
percentile method is used or the highest density interval is chosen to
derive a confidence interval for the combined parameter with the desired
coverage. References: Davison and Hinkley (1997,ISBN:0-521-57471-4) for
the parametric bootstrap and percentile method, Gelman et al.
(2014,ISBN:978-1-4398-4095-5) for the highest density interval, Stockdale
et al. (2020)<doi:10.1016/j.jhep.2020.04.008> for an example of combining
conditional prevalences.

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
