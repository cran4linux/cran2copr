%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dcorVS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection Algorithms Using the Distance Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dcov 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
Requires:         R-CRAN-dcov 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 

%description
The 'FBED' and 'mmpc' variable selection algorithms have been implemented
using the distance correlation. The references include: Tsamardinos I.,
Aliferis C. F. and Statnikov A. (2003). "Time and sample efficient
discovery of Markovblankets and direct causal relations". In Proceedings
of the ninth ACM SIGKDD international Conference.
<doi:10.1145/956750.956838>. Borboudakis G. and Tsamardinos I. (2019).
"Forward-backward selection with early dropping". Journal of Machine
Learning Research, 20(8): 1--39. <doi:10.48550/arXiv.1705.10770>. Huo X.
and Szekely G.J. (2016). "Fast computing for distance covariance".
Technometrics, 58(4): 435--447. <doi:10.1080/00401706.2015.1054435>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
