%global __brp_check_rpaths %{nil}
%global packname  RProbSup
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Probability of Superiority

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The A() function calculates the A statistic, a nonparametric measure of
effect size for two independent groups that’s also known as the
probability of superiority (Ruscio, 2008), along with its standard error
and a confidence interval constructed using bootstrap methods (Ruscio &
Mullen, 2012). Optional arguments can be specified to calculate variants
of the A statistic developed for other research designs (e.g., related
samples, more than two independent groups or related samples; Ruscio &
Gera, 2013). <DOI: 10.1037/1082-989X.13.1.19>. <DOI:
10.1080/00273171.2012.658329>. <DOI: 10.1080/00273171.2012.738184>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
