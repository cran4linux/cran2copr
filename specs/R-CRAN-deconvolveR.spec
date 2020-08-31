%global packname  deconvolveR
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Bayes Estimation Strategies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-splines 
Requires:         R-stats 

%description
Empirical Bayes methods for learning prior distributions from data. An
unknown prior distribution (g) has yielded (unobservable) parameters, each
of which produces a data point from a parametric exponential family (f).
The goal is to estimate the unknown prior ("g-modeling") by deconvolution
and Empirical Bayes methods. Details and examples are in the paper by
Narasimhan and Efron (2020, <doi:10.18637/jss.v094.i11>).

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
