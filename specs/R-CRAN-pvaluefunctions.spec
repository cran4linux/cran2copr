%global packname  pvaluefunctions
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          2%{?dist}
Summary:          Creates and Plots P-Value Functions, S-Value Functions,Confidence Distributions and Confidence Densities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-pracma >= 2.2.9
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-zipfR >= 0.6.66
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-pracma >= 2.2.9
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-zipfR >= 0.6.66
Requires:         R-stats 

%description
Contains functions to compute and plot confidence distributions,
confidence densities, p-value functions and s-value (surprisal) functions
for several commonly used estimates. Instead of just calculating one
p-value and one confidence interval, p-value functions display p-values
and confidence intervals for many levels thereby allowing to gauge the
compatibility of several parameter values with the data. These methods are
discussed by Infanger D, Schmidt-Trucksäss A. (2019)
<doi:10.1002/sim.8293>; Poole C. (1987) <doi:10.2105/AJPH.77.2.195>;
Schweder T, Hjort NL. (2002) <doi:10.1111/1467-9469.00285>; Bender R, Berg
G, Zeeb H. (2005) <doi:10.1002/bimj.200410104> ; Singh K, Xie M,
Strawderman WE. (2007) <doi:10.1214/074921707000000102>; Rothman KJ,
Greenland S, Lash TL. (2008, ISBN:9781451190052); Amrhein V, Trafimow D,
Greenland S. (2019) <doi:10.1080/00031305.2018.1543137>; and Greenland S.
(2019) <doi:10.1080/00031305.2018.1529625>.

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

%files
%{rlibdir}/%{packname}
