%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IBFS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Initial Basic Feasible Solution for Transportation Problem

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The initial basic feasible solution (IBFS) is a significant step to
achieve the minimal total cost (optimal solution) of the transportation
problem. However, the existing methods of IBFS do not always provide a
good feasible solution which can reduce the number of iterations to find
the optimal solution. This initial basic feasible solution can be obtained
by using any of the following methods. a) North West Corner Method. b)
Least Cost Method. c) Row Minimum Method. d) Column Minimum Method. e)
Vogel's Approximation Method. etc. For more technical details about the
algorithms please refer below URLs.
<https://theintactone.com/2018/05/24/ds-u2-topic-8-transportation-problems-initial-basic-feasible-solution/>.
<https://www.brainkart.com/article/Methods-of-finding-initial-Basic-Feasible-Solutions_39037/>.
<https://myhomeworkhelp.com/row-minima-method/>.
<https://myhomeworkhelp.com/column-minima-method/>.

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
