%global packname  orders
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Sampling from Order Statistics of New Families of Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Newdistns 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-CRAN-Newdistns 
Requires:         R-CRAN-gamlss.dist 

%description
Set of tools to generate samples of order statistics and others quantities
of interest from new families of distributions. The main references for
this package are: Gentle, J. (2009), Computational Statistics,
Springer-Verlag; Naradajah, S. and Rocha, R. (2016),
<DOI:10.18637/jss.v069.i10> and Stasinopoulos, M. and Rigby, R. (2015),
<DOI:10.1111/j.1467-9876.2005.00510.x>. The families of distributions are:
Marshall Olkin G distributions, exponentiated G distributions, beta G
distributions, gamma G distributions, Kumaraswamy G distributions,
generalized beta G distributions, beta extended G distributions, gamma G
distributions, gamma uniform G distributions, beta exponential G
distributions, Weibull G distributions, log gamma G I distributions, log
gamma G II distributions, exponentiated generalized G distributions,
exponentiated Kumaraswamy G distributions, geometric exponential Poisson G
distributions, truncated-exponential skew-symmetric G distributions,
modified beta G distributions, and exponentiated exponential Poisson G
distributions, Poisson-inverse gaussian distribution, Skew normal type 1
distributions, Skew student t distribution, Sinh-Arcsinh distribution,
Sichel distribution and Zero inflated Poisson.

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
