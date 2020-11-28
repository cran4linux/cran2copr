%global packname  IMEC
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ising Model of Explanatory Coherence

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-IsingSampler 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-qgraph 
Requires:         R-CRAN-IsingSampler 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-qgraph 

%description
Theories are one of the most important tools of science. Although
psychologists discussed problems of theory in their discipline for a long
time, weak theories are still widespread in most subfields. One possible
reason for this is that psychologists lack the tools to systematically
assess the quality of their theories. Previously a computational model for
formal theory evaluation based on the concept of explanatory coherence was
developed (Thagard, 1989, <doi:10.1017/S0140525X00057046>). However, there
are possible improvements to this model and it is not available in
software that psychologists typically use. Therefore, a new implementation
of explanatory coherence based on the Ising model is available in this
R-package.

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
