%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMX
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Rasch Models -- eXtensions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Extend Rasch and Item Response Theory (IRT) analyses by providing tools
for post-processing the output from five major IRT packages (i.e., 'eRm',
'psychotools', 'ltm', 'mirt', and 'TAM'). The current version provides the
plotPIccc() function, which extracts from the return object of the
originating package all information required to draw an extended
Person-Item-Map (PIccc), showing any combination of * category
characteristic curves (CCCs), * threshold characteristic curves (TCCs), *
item characteristic curves (ICCs), * category information functions
(CIFs), * item information functions (IIFs), * test information function
(TIF), and the * standard error curve (S.E.). for uni- and
multidimensional models (as far as supported by each package). It allows
for selecting dimensions, items, and categories to plot and offers
numerous options to adapt the output. The return object contains all
calculated values for further processing.

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
