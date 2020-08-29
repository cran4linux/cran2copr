%global packname  haplo.stats
%global packver   1.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.5
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis of Haplotypes with Traits and Covariateswhen Linkage Phase is Ambiguous

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-arsenal 
BuildRequires:    R-CRAN-rms 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-arsenal 
Requires:         R-CRAN-rms 

%description
Routines for the analysis of indirectly measured haplotypes. The
statistical methods assume that all subjects are unrelated and that
haplotypes are ambiguous (due to unknown linkage phase of the genetic
markers). The main functions are: haplo.em(), haplo.glm(), haplo.score(),
and haplo.power(); all of which have detailed examples in the vignette.

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
