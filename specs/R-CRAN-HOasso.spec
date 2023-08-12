%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HOasso
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Higher Order Assortativity for Complex Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Rdpack 

%description
Allows to evaluate Higher Order Assortativity of complex networks defined
through objects of class 'igraph' from the package of the same name. The
package returns a result also for directed and weighted graphs.
References, Arcagni, A., Grassi, R., Stefani, S., & Torriero, A. (2017)
<doi:10.1016/j.ejor.2017.04.028> Arcagni, A., Grassi, R., Stefani, S., &
Torriero, A. (2021) <doi:10.1016/j.jbusres.2019.10.008> Arcagni, A.,
Cerqueti, R., & Grassi, R. (2023) <doi:10.48550/arXiv.2304.01737>.

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
