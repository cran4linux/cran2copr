%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AMCP
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Sets to Accompany Designing Experiments and Analyzing Data: A Model Comparison Perspective (Maxwell, Delaney, and Kelley, 2027, 4th Edition)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch

%description
Data sets that accompany the book "Designing experiments and analyzing
data: A model comparison perspective" (4th ed.) by Maxwell, Delaney, and
Kelley (2027; ISBN 978-1-041-25384-6; Routledge). Contains all of the data
sets in the book's chapters and end-of-chapter exercises. Beginning with
version 2.0, the package is tailored to the 4th edition of the book; for
the data as distributed with the 3rd edition (2018), install the archived
version 1.0.2 from CRAN. We recommend the 'DMAR' package as the companion
for carrying out the book's analyses; these analyses are illustrated in
the book itself using the 'MBESS' package, which may be used as well. The
book's companion website is available at
<https://designingexperiments.com/> and its publisher page at
<https://www.routledge.com/Designing-Experiments-and-Analyzing-Data-A-Model-Comparison-Perspective/Maxwell-Delaney-Kelley/p/book/9781041253846>.

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
