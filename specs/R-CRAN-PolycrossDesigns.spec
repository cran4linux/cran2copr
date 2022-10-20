%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PolycrossDesigns
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Polycross Designs ("PolycrossDesigns"")

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
A polycross is the pollination by natural hybridization of a group of
genotypes, generally selected, grown in isolation from other compatible
genotypes in such a way to promote random open pollination. A particular
practical application of the polycross method occurs in the production of
a synthetic variety resulting from cross-pollinated plants. Laying out
these experiments in appropriate designs, known as polycross designs,
would not only save experimental resources but also gather more
information from the experiment. Different experimental situations may
arise in polycross nurseries which may be requiring different polycross
designs (Varghese et. al. (2015) <doi:10.1080/02664763.2015.1043860>. "
Experimental designs for open pollination in polycross trials"). This
package contains a function named PD() which generates nine types of
polycross designs suitable for various experimental situations.

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
