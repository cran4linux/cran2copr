%global packname  BDEsize
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Determination of Sample Size in Balanced Design of Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fpow 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-fpow 
Requires:         R-CRAN-ggplot2 

%description
For a balanced design of experiments, this package calculates the sample
size required to detect a certain standardized effect size, under a
significance level. This package also provides three graphs; detectable
standardized effect size vs power, sample size vs detectable standardized
effect size, and sample size vs power, which show the mutual relationship
between the sample size, power and the detectable standardized effect
size. The detailed procedure is described in R. V. Lenth (2006-9)
<https://homepage.divms.uiowa.edu/~rlenth/Power/>, Y. B. Lim (1998), M. A.
Kastenbaum, D. G. Hoel and K. O. Bowman (1970) <doi:10.2307/2334851>, and
Douglas C. Montgomery (2013, ISBN: 0849323312).

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
